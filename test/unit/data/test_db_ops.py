from datetime import date

import pytest
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from src.data import db_ops, models

# Create a new engine for an in-memory SQLite database
engine = create_engine("sqlite:///:memory:")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the tables in the database
models.Base.metadata.create_all(bind=engine)


@pytest.fixture
def db():
    # Create a new session
    db = SessionLocal()
    yield db
    # Close the session after the test is done
    db.close()


# Define the tables and inputs
tables_and_inputs = [
    (
        "basic_info",
        {
            "name": "John Doe",
            "email": "john.doe@hotmail.com",
            "phone": "1234567890",
            "website": "https://www.johndoe.com",
            "linkedin": "https://www.linkedin.com/in/johndoe",
            "github": "https://www.github.com/johndoe",
            "intro": "Hello, I'm John Doe!",
        },
    ),
    (
        "education",
        {
            "institution": "MIT",
            "degree": "BSc Computer Science",
            "duration_start": date(2015, 9, 1),
            "duration_end": date(2019, 6, 1),
            "fk_user": 1,
        },
    ),
    (
        "experience",
        {
            "company": "Google",
            "title": "Software Engineer",
            "duration_start": date(2019, 6, 1),
            "tech_stack": "Python, SQL, Docker",
            "fk_user": 1,
        },
    ),
    (
        "projects",
        {
            "title": "My Awesome Project",
            "description": "This is my awesome project",
            "fk_user": 1,
        },
    ),
    (
        "skills",
        {
            "skill": "Python",
            "subcategory": "Programming Languages",
            "proficiency": "Advanced",
            "fk_user": 1,
        },
    ),
    (
        "certifications",
        {
            "title": "Google Cloud Professional Data Engineer",
            "issuer": "Google",
            "achievement_date": date(2020, 1, 1),
            "fk_user": 1,
        },
    ),
    (
        "honors_and_awards",
        {
            "title": "Best Employee",
            "description": "From Google",
            "fk_user": 1,
        },
    ),
    (
        "interests",
        {
            "interest": "Basketball",
            "subcategory": "Sports",
            "fk_user": 1,
        },
    ),
]


@pytest.mark.parametrize("table_name,input_data", tables_and_inputs)
def test_add_data_to_table(db: Session, table_name: str, input_data: dict):
    added_data = db_ops.add_data_to_table(db, table_name, input_data)
    # Verify that the data was added correctly
    for key, value in input_data.items():
        assert getattr(added_data, key) == value


def test_add_data_to_table_invalid(db: Session):
    # Because of the unique constraint on the email and phone field, adding the same data again should raise an error
    with pytest.raises(IntegrityError):
        db_ops.add_data_to_table(db, tables_and_inputs[0][0], tables_and_inputs[0][1])


@pytest.mark.parametrize("table_name,input_data", tables_and_inputs)
def test_read_data_from_table(db: Session, table_name: str, input_data: dict):
    read_data = db_ops.read_data_from_table(db, table_name)
    # Verify that the data was added correctly
    for key, value in input_data.items():
        assert getattr(read_data[0], key) == value


@pytest.mark.parametrize("table_name,input_data", tables_and_inputs)
def test_read_single_data(db: Session, table_name: str, input_data: dict):
    read_data = db_ops.read_single_data(db, table_name)
    # Verify that the data was added correctly
    for key, value in input_data.items():
        assert getattr(read_data, key) == value


@pytest.mark.parametrize("table_name,input_data", tables_and_inputs)
def test_filter_data_with_id(db: Session, table_name: str, input_data: dict):
    filtered_data = db_ops.filter_data_with_id(db, table_name, 1)
    # Verify that the data was added correctly
    for key, value in input_data.items():
        assert getattr(filtered_data, key) == value


@pytest.mark.parametrize("table_name,input_data", tables_and_inputs)
def test_filter_data_from_table(db: Session, table_name: str, input_data: dict):
    single_key = list(input_data.keys())[0]
    filtered_data = db_ops.filter_data_from_table(db, table_name, {single_key: input_data[single_key]})
    # Verify that the data was added correctly
    for key, value in input_data.items():
        assert getattr(filtered_data[0], key) == value


@pytest.mark.parametrize("table_name,input_data", tables_and_inputs)
def test_update_data_with_id(db: Session, table_name: str, input_data: dict):
    single_key = list(input_data.keys())[0]
    updated_data = db_ops.update_data_with_id(db, table_name, 1, {single_key: "Updated"})
    assert getattr(updated_data, single_key) == "Updated"


def test_snake_to_pascal_case():
    assert db_ops.snake_to_pascal_case("hello_world") == "HelloWorld"
