from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.data.db_init import Base


class BasicInfo(Base):
    __tablename__ = "basic_info"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    location = Column(String)
    website = Column(String)
    linkedin = Column(String)
    github = Column(String)


class Education(Base):
    __tablename__ = "education"

    id = Column(Integer, primary_key=True, index=True)
    institution = Column(String)
    location = Column(String)
    duration_start = Column(DateTime)
    duration_end = Column(DateTime)
    degree = Column(String)
    major = Column(String)
    minor = Column(String)
    gpa = Column(String)
    courses = Column(String)
    user = Column(Integer, ForeignKey("basic_info.id"))


class Experience(Base):
    __tablename__ = "experience"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String)
    location = Column(String)
    title = Column(String)
    duration_start = Column(DateTime)
    duration_end = Column(DateTime)
    description = Column(String)


class Skills(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    skill = Column(String)
    subcategory = Column(String)
    proficiency = Column(String)


class Projects(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)


class Certifications(Base):
    __tablename__ = "certifications"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    date = Column(DateTime)
    link = Column(String)


class HonorsAndAwards(Base):
    __tablename__ = "honors_and_awards"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)


class Interests(Base):
    __tablename__ = "interests"

    id = Column(Integer, primary_key=True, index=True)
    interest = Column(String)
    subcategory = Column(String)
