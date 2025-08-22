from datetime import timedelta

from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from src.auth import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    AdminUser,
    authenticate_admin,
    create_access_token,
    get_current_admin_from_cookie,
)
from src.data import db_init, db_ops

router = APIRouter(prefix="/admin", tags=["admin"])
templates = Jinja2Templates(directory="templates")

# Available table names
AVAILABLE_TABLES = [
    "basic_info",
    "education",
    "experience",
    "skills",
    "projects",
    "certifications",
    "honors_and_awards",
    "interests",
    "resume",
]


@router.get("/login", response_class=HTMLResponse)
async def admin_login_page(request: Request):
    """Display admin login page"""
    return templates.TemplateResponse("admin/login.html", {"request": request})


@router.post("/login")
async def admin_login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
):
    """Handle admin login and set JWT cookie"""
    if not authenticate_admin(username, password):
        response = templates.TemplateResponse(
            "admin/login.html", {"request": request, "error": "Invalid username or password"}
        )
        response.status_code = 400
        return response
    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": username}, expires_delta=access_token_expires)

    # Redirect to dashboard and set cookie
    response = RedirectResponse(url="/admin/dashboard", status_code=302)
    response.set_cookie(
        key="access_token",
        value=f"Bearer {access_token}",
        httponly=True,
        max_age=ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        path="/",
        samesite="lax",
        secure=False,  # Set to True in production with HTTPS
    )

    return response


@router.get("/logout")
async def admin_logout():
    """Handle admin logout and clear cookie"""
    response = RedirectResponse(url="/", status_code=302)
    response.delete_cookie(key="access_token")
    return response


@router.get("/dashboard", response_class=HTMLResponse)
async def admin_dashboard(
    request: Request,
    current_admin: AdminUser = Depends(get_current_admin_from_cookie),
    db: Session = Depends(db_init.get_db),
):
    """Display admin dashboard with all users"""
    try:
        users = db_ops.read_data_from_table(db, "basic_info")
        return templates.TemplateResponse(
            "admin/dashboard.html", {"request": request, "users": users, "current_admin": current_admin.username}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.get("/user/{user_id}", response_class=HTMLResponse)
async def admin_user_panel(
    request: Request,
    user_id: int,
    current_admin: AdminUser = Depends(get_current_admin_from_cookie),
    db: Session = Depends(db_init.get_db),
):
    """Display user panel with all tables for a specific user"""
    try:
        # Get user info
        user = db_ops.filter_data_with_id(db, "basic_info", user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # Get data for each table
        table_data = {}
        for table_name in AVAILABLE_TABLES:
            if table_name == "basic_info":
                table_data[table_name] = [user]  # Always 1 basic_info per user
            else:
                try:
                    data = db_ops.filter_data_from_table(db, table_name, {"fk_user": user_id})
                    table_data[table_name] = data if data else []
                except Exception:
                    table_data[table_name] = []

        return templates.TemplateResponse(
            "admin/user_panel.html",
            {
                "request": request,
                "user": user,
                "table_data": table_data,
                "table_names": AVAILABLE_TABLES,
                "current_admin": current_admin.username,
            },
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.get("/user/{user_id}/table/{table_name}", response_class=HTMLResponse)
async def admin_edit_table(
    request: Request,
    user_id: int,
    table_name: str,
    current_admin: AdminUser = Depends(get_current_admin_from_cookie),
    db: Session = Depends(db_init.get_db),
):
    """Display table editing interface"""
    if table_name not in AVAILABLE_TABLES:
        raise HTTPException(status_code=404, detail="Table not found")

    try:
        # Get user info
        user = db_ops.filter_data_with_id(db, "basic_info", user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # Get table data
        if table_name == "basic_info":
            table_data = [user]
        else:
            table_data = db_ops.filter_data_from_table(db, table_name, {"fk_user": user_id})

        # Convert SQLAlchemy objects to dictionaries
        records = []
        if table_data:
            for record in table_data:
                if hasattr(record, "__dict__"):
                    record_dict = {key: value for key, value in record.__dict__.items() if not key.startswith("_")}
                    records.append(record_dict)
                else:
                    records.append(record)

        # Get model class to understand field structure
        model_class = db_ops.get_model_class_from_table_name(table_name)

        # Get field names for the template
        sample_fields = [column.name for column in model_class.__table__.columns]

        return templates.TemplateResponse(
            "admin/edit_table.html",
            {
                "request": request,
                "user": user,
                "table_name": table_name,
                "records": records,
                "sample_fields": sample_fields,
                "current_admin": current_admin.username,
            },
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.post("/user/{user_id}/table/{table_name}/add")
async def admin_add_record(
    user_id: int,
    table_name: str,
    request: Request,
    current_admin: AdminUser = Depends(get_current_admin_from_cookie),
    db: Session = Depends(db_init.get_db),
):
    """Add new record to table"""
    if table_name not in AVAILABLE_TABLES:
        raise HTTPException(status_code=404, detail="Table not found")

    if table_name == "basic_info":
        raise HTTPException(status_code=400, detail="Cannot add new basic_info records")

    try:
        # Get form data and process only new-record fields (suffix '_new')
        form_data = await request.form()
        data = {}
        for key, value in form_data.items():
            if not key.endswith("_new") or not isinstance(value, str) or not value.strip():
                continue
            field_name = key[:-4]
            # Handle different field types
            if field_name in ["duration_start", "duration_end", "achievement_date"]:
                from datetime import datetime

                data[field_name] = datetime.strptime(value, "%Y-%m-%d").date()
            elif field_name == "is_latest":
                data[field_name] = value.lower() in ["true", "1", "on"]
            elif field_name == "gpa":
                data[field_name] = value
            elif field_name in ["important_links", "description"] and value.startswith(("[", "{")):
                import json

                try:
                    data[field_name] = json.loads(value)
                except Exception:
                    data[field_name] = value
            else:
                data[field_name] = value
        # Add user foreign key
        data["fk_user"] = user_id

        # Add record to database
        db_ops.add_data_to_table(db, table_name, data)

        return RedirectResponse(
            url=f"/admin/user/{user_id}/table/{table_name}?success=Record added successfully", status_code=302
        )

    except Exception as e:
        return RedirectResponse(
            url=f"/admin/user/{user_id}/table/{table_name}?error=Failed to add record: {str(e)}", status_code=302
        )


@router.post("/user/{user_id}/table/{table_name}/update/{record_id}")
async def admin_update_record(
    user_id: int,
    table_name: str,
    record_id: int,
    request: Request,
    current_admin: AdminUser = Depends(get_current_admin_from_cookie),
    db: Session = Depends(db_init.get_db),
):
    """Update existing record in table"""
    if table_name not in AVAILABLE_TABLES:
        raise HTTPException(status_code=404, detail="Table not found")

    try:
        # Get form data
        form_data = await request.form()
        data = {}

        # Process form fields
        for key, value in form_data.items():
            if key != "action" and isinstance(value, str) and value.strip():  # Skip empty values and action field
                # Handle different field types
                if key in ["duration_start", "duration_end", "achievement_date"]:
                    # Date fields
                    from datetime import datetime

                    if value:
                        data[key] = datetime.strptime(value, "%Y-%m-%d").date()
                    else:
                        data[key] = None
                elif key in ["is_latest"]:
                    # Boolean fields
                    data[key] = value.lower() in ["true", "1", "on"] if value else False
                elif key in ["gpa"]:
                    # Keep as string
                    data[key] = value if value else None
                elif key in ["important_links", "description"] and value and value.startswith(("[", "{")):
                    # JSON fields
                    import json

                    try:
                        data[key] = json.loads(value)
                    except Exception:
                        data[key] = value
                else:
                    data[key] = value if value else None

        # Update record in database
        db_ops.update_data_with_id(db, table_name, record_id, data)

        return RedirectResponse(
            url=f"/admin/user/{user_id}/table/{table_name}?success=Record updated successfully", status_code=302
        )

    except Exception as e:
        return RedirectResponse(
            url=f"/admin/user/{user_id}/table/{table_name}?error=Failed to update record: {str(e)}", status_code=302
        )


@router.post("/user/{user_id}/table/{table_name}")
async def admin_save_records(
    user_id: int,
    table_name: str,
    request: Request,
    current_admin: AdminUser = Depends(get_current_admin_from_cookie),
    db: Session = Depends(db_init.get_db),
):
    """Save changes to existing records and add new records"""
    if table_name not in AVAILABLE_TABLES:
        raise HTTPException(status_code=404, detail="Table not found")

    try:
        # Get form data
        form_data = await request.form()
        success_messages = []
        error_messages = []

        # New records are handled by the dedicated `/add` endpoint;
        # The following block for handling new_record_data is removed to prevent double addition.
        # # Process new record fields (inputs named `<field>_new`)
        # new_record_data = {}
        # for key, value in form_data.items():
        #     if key.endswith("_new") and isinstance(value, str) and value.strip():
        #         field_name = key[:-4]  # remove '_new' suffix
        #         new_record_data[field_name] = value
        # if new_record_data:
        #     # Attach user foreign key and insert
        #     new_record_data["fk_user"] = user_id
        #     try:
        #         db_ops.add_data_to_table(db, table_name, new_record_data)
        #         success_messages.append("New record added successfully")
        #     except Exception as e:
        #         error_messages.append(f"Failed to add new record: {str(e)}")

        # Process existing records
        record_count = 0
        if "record_count" in form_data:
            count_val = form_data.get("record_count")
            if isinstance(count_val, str) and count_val.isdigit():
                record_count = int(count_val)

        for i in range(record_count):
            record_id_key = f"record_id_{i}"
            if record_id_key in form_data:
                id_val = form_data.get(record_id_key)
                if isinstance(id_val, str) and id_val.isdigit():
                    record_id = int(id_val)
                    record_data = {}

                    # Gather all fields for this record
                    for key, value in form_data.items():
                        if isinstance(key, str) and isinstance(value, str):
                            if key.endswith(f"_{i}") and not key.startswith("record_id_"):
                                field_name = key.rsplit("_", 1)[0]
                                record_data[field_name] = value

                    if record_data:
                        # Update record in database
                        db_ops.update_data_with_id(db, table_name, record_id, record_data)
                        success_messages.append(f"Record #{i + 1} updated successfully")

        # Construct response with appropriate messages
        if error_messages:
            return RedirectResponse(
                url=f"/admin/user/{user_id}/table/{table_name}?error={' | '.join(error_messages)}", status_code=302
            )
        else:
            return RedirectResponse(
                url=f"/admin/user/{user_id}/table/{table_name}?success={' | '.join(success_messages or ['Changes saved successfully'])}",
                status_code=302,
            )

    except Exception as e:
        return RedirectResponse(
            url=f"/admin/user/{user_id}/table/{table_name}?error=Failed to process form: {str(e)}", status_code=302
        )


@router.post("/user/{user_id}/table/{table_name}/delete/{record_id}")
async def admin_delete_record(
    user_id: int,
    table_name: str,
    record_id: int,
    current_admin: AdminUser = Depends(get_current_admin_from_cookie),
    db: Session = Depends(db_init.get_db),
):
    """Delete record from table"""
    if table_name not in AVAILABLE_TABLES:
        raise HTTPException(status_code=404, detail="Table not found")

    if table_name == "basic_info":
        raise HTTPException(status_code=400, detail="Cannot delete basic_info records")

    try:
        # Delete record from database
        db_ops.delete_data_by_id(db, table_name, record_id)

        return RedirectResponse(
            url=f"/admin/user/{user_id}/table/{table_name}?success=Record deleted successfully", status_code=302
        )

    except Exception as e:
        return RedirectResponse(
            url=f"/admin/user/{user_id}/table/{table_name}?error=Failed to delete record: {str(e)}", status_code=302
        )
