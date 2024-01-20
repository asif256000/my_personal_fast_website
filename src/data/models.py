from sqlalchemy import JSON, Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .db_init import Base


class BasicInfo(Base):
    __tablename__ = "basic_info"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String, unique=True)
    location = Column(String)
    website = Column(String)
    linkedin = Column(String)
    github = Column(String)
    intro = Column(String)

    education = relationship("Education", back_populates="user")
    experience = relationship("Experience", back_populates="user")
    skills = relationship("Skills", back_populates="user")
    projects = relationship("Projects", back_populates="user")
    certifications = relationship("Certifications", back_populates="user")
    honors_and_awards = relationship("HonorsAndAwards", back_populates="user")
    interests = relationship("Interests", back_populates="user")
    resume = relationship("Resume", back_populates="user")


class Education(Base):
    __tablename__ = "education"

    id = Column(Integer, primary_key=True, index=True)
    institution = Column(String)
    institution_logo = Column(String)
    institution_link = Column(String)
    location = Column(String)
    duration_start = Column(Date)
    duration_end = Column(Date)
    degree = Column(String)
    major = Column(String)
    minor = Column(String)
    gpa = Column(String)
    courses = Column(String)
    important_links = Column(JSON)
    fk_user = Column(Integer, ForeignKey("basic_info.id"))

    user = relationship("BasicInfo", back_populates="education")


class Experience(Base):
    __tablename__ = "experience"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String)
    company_logo = Column(String)
    company_link = Column(String)
    location = Column(String)
    title = Column(String)
    duration_start = Column(Date)
    duration_end = Column(Date)
    description = Column(JSON)
    important_links = Column(JSON)
    tech_stack = Column(String)
    fk_user = Column(Integer, ForeignKey("basic_info.id"))

    user = relationship("BasicInfo", back_populates="experience")


class Skills(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    skill = Column(String)
    subcategory = Column(String)
    proficiency = Column(String)
    fk_user = Column(Integer, ForeignKey("basic_info.id"))

    user = relationship("BasicInfo", back_populates="skills")


class Projects(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    link = Column(String)
    fk_user = Column(Integer, ForeignKey("basic_info.id"))

    user = relationship("BasicInfo", back_populates="projects")


class Certifications(Base):
    __tablename__ = "certifications"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    issuer = Column(String)
    description = Column(String)
    achievement_date = Column(Date)
    link = Column(String)
    fk_user = Column(Integer, ForeignKey("basic_info.id"))

    user = relationship("BasicInfo", back_populates="certifications")


class HonorsAndAwards(Base):
    __tablename__ = "honors_and_awards"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    fk_user = Column(Integer, ForeignKey("basic_info.id"))

    user = relationship("BasicInfo", back_populates="honors_and_awards")


class Interests(Base):
    __tablename__ = "interests"

    id = Column(Integer, primary_key=True, index=True)
    interest = Column(String)
    subcategory = Column(String)
    fk_user = Column(Integer, ForeignKey("basic_info.id"))

    user = relationship("BasicInfo", back_populates="interests")


class Resume(Base):
    __tablename__ = "resume"

    id = Column(Integer, primary_key=True, index=True)
    file_path = Column(String)
    is_latest = Column(Boolean)
    fk_user = Column(Integer, ForeignKey("basic_info.id"))

    user = relationship("BasicInfo", back_populates="resume")
