from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import Session

from . import models, schemas


def snake_to_camel_case(string: str):
    return "".join(word.capitalize() for word in string.split("_"))


def get_model_class_from_table_name(table_name: str) -> models.Base:
    try:
        model_class = getattr(models, snake_to_camel_case(table_name))
    except AttributeError:
        return ValueError(f"Table name: {table_name} is not valid")
    return model_class


def get_schema_class_from_table_name(table_name: str) -> schemas.BaseModel:
    try:
        schema_class = getattr(schemas, snake_to_camel_case(table_name) + "Create")
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
        return ValueError(f"Data: {data} is not valid for table {table_name}.\nError: {e}")


def read_from_table(db: Session, table_name: str):
    model_class = get_model_class_from_table_name(table_name)

    table = db.query(model_class).all()
    return table


def read_one_from_table(db: Session, table_name: str):
    model_class = get_model_class_from_table_name(table_name)

    table = db.query(model_class).first()
    return table


def filter_from_table_with_id(db: Session, table_name: str, id: int):
    model_class = get_model_class_from_table_name(table_name)

    table = db.query(model_class).filter(model_class.id == id).first()
    return table


def filter_from_table(db: Session, table_name: str, filter: dict):
    model_class = get_model_class_from_table_name(table_name)

    table = db.query(model_class).filter_by(**filter).all()
    return table


def update_data_in_table(db: Session, table_name: str, id: int, data: dict):
    table_data = filter_from_table_with_id(db, table_name, id)
    if table_data is None:
        return ValueError(f"No data found in table {table_name} with id {id}")

    for key, value in data.items():
        if hasattr(table_data, key):
            setattr(table_data, key, value)

    try:
        db.commit()
        db.refresh(table_data)
        return table_data
    except InvalidRequestError as e:
        db.rollback()
        return ValueError(f"Data: {data} is not valid for table {table_name}.\nError: {e}")
