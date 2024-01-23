import pytest
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200


def test_read_overview():
    response = client.get("/overview")
    assert response.status_code == 200


def test_read_experience_education():
    response = client.get("/experience_education")
    assert response.status_code == 200


def test_read_projects_certificates():
    response = client.get("/projects_certificates")
    assert response.status_code == 200


def test_read_awards_interests():
    response = client.get("/awards_interests")
    assert response.status_code == 200


def test_read_resume():
    response = client.get("/resume")
    assert response.status_code == 200
