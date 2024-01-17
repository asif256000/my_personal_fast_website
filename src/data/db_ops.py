from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import Session

from . import models, schemas


def snake_to_camel_case(string: str):
    return "".join(word.capitalize() for word in string.split("_"))


def add_data_to_table(db: Session, table_name: str, data: dict):
    try:
        model_class = getattr(models, snake_to_camel_case(table_name))
    except AttributeError:
        return ValueError(f"Table name: {table_name} is not valid")

    schema_class = getattr(schemas, snake_to_camel_case(table_name) + "Create")
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
    try:
        model_class = getattr(models, snake_to_camel_case(table_name))
    except AttributeError:
        return ValueError(f"Table name: {table_name} is not valid")

    table = db.query(model_class).all()
    return table


def read_one_from_table(db: Session, table_name: str):
    try:
        model_class = getattr(models, snake_to_camel_case(table_name))
    except AttributeError:
        return ValueError(f"Table name: {table_name} is not valid")

    table = db.query(model_class).first()
    return table


def filter_from_table_with_id(db: Session, table_name: str, id: int):
    try:
        model_class = getattr(models, snake_to_camel_case(table_name))
    except AttributeError:
        return ValueError(f"Table name: {table_name} is not valid")

    table = db.query(model_class).filter(model_class.id == id).first()
    return table


def filter_from_table(db: Session, table_name: str, filter: dict):
    try:
        model_class = getattr(models, snake_to_camel_case(table_name))
    except AttributeError:
        return ValueError(f"Table name: {table_name} is not valid")

    table = db.query(model_class).filter_by(**filter).all()
    return table


def update_data_in_table(db: Session, table_name: str, id: int, data: dict):
    try:
        model_class = getattr(models, snake_to_camel_case(table_name))
    except AttributeError:
        return ValueError(f"Table name: {table_name} is not valid")

    schema_class = getattr(schemas, snake_to_camel_case(table_name) + "Create")
    table_data = schema_class(**data)
    table_instance = model_class(**table_data.model_dump())
    try:
        db.query(model_class).filter(model_class.id == id).update(table_instance)
        db.commit()
        db.refresh(table_instance)
        return table_instance
    except InvalidRequestError as e:
        db.rollback()
        return ValueError(f"Data: {data} is not valid for table {table_name}.\nError: {e}")
