from datetime import date

from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from src.data import db_init, db_ops, models, schemas
from src.main import app

models.Base.metadata.create_all(bind=db_init.engine)
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


def get_db():
    try:
        db = db_init.SessionLocal()
        yield db
    finally:
        db.close()


def arrange_skills(all_skills):
    arranged_skills = {}
    for skill in all_skills:
        if skill.subcategory not in arranged_skills:
            arranged_skills[skill.subcategory] = {skill.proficiency: [skill.skill]}
        else:
            if skill.proficiency not in arranged_skills[skill.subcategory]:
                arranged_skills[skill.subcategory][skill.proficiency] = [skill.skill]
            else:
                arranged_skills[skill.subcategory][skill.proficiency].append(skill.skill)

    return arranged_skills


def arrange_interests(all_interests):
    arranged_interests = {}
    for interest in all_interests:
        if interest.subcategory not in arranged_interests:
            arranged_interests[interest.subcategory] = [interest.interest]
        else:
            arranged_interests[interest.subcategory].append(interest.interest)

    return arranged_interests


@app.get("/profile", name="profile", response_class=HTMLResponse)
def read_profile(request: Request, db: Session = Depends(get_db)):
    basic_info = db_ops.read_one_from_table(db, table_name="basic_info")
    user_filter = {"fk_user": basic_info.id}

    education = db_ops.filter_from_table(db, table_name="education", filter=user_filter)
    experience = db_ops.filter_from_table(db, table_name="experience", filter=user_filter)

    skills = db_ops.filter_from_table(db, table_name="skills", filter=user_filter)
    projects = db_ops.filter_from_table(db, table_name="projects", filter=user_filter)
    certifications = db_ops.filter_from_table(db, table_name="certifications", filter=user_filter)
    honors_and_awards = db_ops.filter_from_table(db, table_name="honors_and_awards", filter=user_filter)
    interests = db_ops.filter_from_table(db, table_name="interests", filter=user_filter)
    resume = db_ops.filter_from_table(db, table_name="resume", filter=user_filter | {"is_latest": 1})

    return templates.TemplateResponse(
        "profile.html",
        {
            "request": request,
            "curr_date": date.today(),
            "basic_info": basic_info,
            "education": education,
            "experience": experience,
            "skills": arrange_skills(skills),
            "projects": projects,
            "certifications": certifications,
            "honors_and_awards": honors_and_awards,
            "interests": arrange_interests(interests),
            "resume": resume,
        },
    )


@app.get("/", name="home", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
