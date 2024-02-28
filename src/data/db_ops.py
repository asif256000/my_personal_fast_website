from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import Session

from . import models, schemas


def snake_to_pascal_case(string: str):
    return "".join(word.capitalize() for word in string.split("_"))


def get_model_class_from_table_name(table_name: str) -> models.Base:
    try:
        model_class = getattr(models, snake_to_pascal_case(table_name))
    except AttributeError:
        return ValueError(f"Table name: {table_name} is not valid")
    return model_class


def get_schema_class_from_table_name(table_name: str) -> schemas.BaseModel:
    try:
        schema_class = getattr(schemas, snake_to_pascal_case(table_name) + "Create")
    except AttributeError:
        return ValueError(f"Table name: {table_name} is not valid")
    return schema_class


def add_data_to_table(db: Session, table_name: str, data: dict):
    model_class = get_model_class_from_table_name(table_name)
    schema_class = get_schema_class_from_table_name(table_name)

    table_data = schema_class(**data)
    table_instance = model_class(**table_data.model_dump())
    try:
        db.add(table_instance)
        db.commit()
        db.refresh(table_instance)
        return table_instance
    except InvalidRequestError as e:
        db.rollback()
        raise ValueError(f"Data: {data} is not valid for table {table_name}.\nError: {e}") from e


def delete_data_by_id(db: Session, table_name: str, lookup_id: int):
    record = filter_data_with_id(db, table_name, lookup_id)

    if record:
        try:
            db.delete(record)
            db.commit()
            return record
        except InvalidRequestError as e:
            db.rollback()
            raise ValueError(f"Failed to delete record with ID {lookup_id} from table {table_name}.\nError: {e}") from e
    else:
        return ValueError(
            f"There is no record with id {lookup_id} in table {table_name}. Returning without deleting any data."
        )


def read_data_from_table(db: Session, table_name: str):
    model_class = get_model_class_from_table_name(table_name)

    table = db.query(model_class).all()
    return table


def read_single_data(db: Session, table_name: str):
    model_class = get_model_class_from_table_name(table_name)

    table = db.query(model_class).first()
    return table


def filter_data_with_id(db: Session, table_name: str, lookup_id: int):
    model_class = get_model_class_from_table_name(table_name)

    table = db.query(model_class).filter(model_class.id == lookup_id).first()
    return table


def filter_data_from_table(db: Session, table_name: str, lookup_filter: dict):
    model_class = get_model_class_from_table_name(table_name)

    table = db.query(model_class).filter_by(**lookup_filter).all()
    return table


def update_data_with_id(db: Session, table_name: str, lookup_id: int, data: dict):
    table_data = filter_data_with_id(db, table_name, lookup_id)
    if table_data is None:
        return ValueError(f"No data found in table {table_name} with id {lookup_id}")

    for key, value in data.items():
        if hasattr(table_data, key):
            setattr(table_data, key, value)

    try:
        db.commit()
        db.refresh(table_data)
        return table_data
    except InvalidRequestError as e:
        db.rollback()
        raise ValueError(f"Data: {data} is not valid for table {table_name}.\nError: {e}") from e
