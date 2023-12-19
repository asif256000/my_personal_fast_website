from datetime import datetime

from pydantic import BaseModel


class BasicInfoBase(BaseModel):
    name: str
    email: str
    phone: str | None = None
    location: str | None = None
    website: str | None = None
    linkedin: str | None = None
    github: str | None = None


class BasicInfoCreate(BasicInfoBase):
    name: str
    email: str
    phone: str | None = None
    location: str | None = None
    website: str | None = None
    linkedin: str | None = None
    github: str | None = None


class BasicInfo(BasicInfoBase):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True


class EducationBase(BaseModel):
    institution: str
    location: str | None = None
    duration_start: datetime
    duration_end: datetime | None = None
    degree: str
    major: str | None = None
    minor: str | None = None
    gpa: str | None = None
    courses: str | None = None


class EducationCreate(EducationBase):
    pass


class Education(EducationBase):
    id: int
    institution: str
    degree: str

    class Config:
        orm_mode = True


class ExperienceBase(BaseModel):
    company: str
    location: str | None = None
    title: str
    duration_start: datetime
    duration_end: datetime | None = None
    description: str | None = None


class ExperienceCreate(ExperienceBase):
    pass


class Experience(ExperienceBase):
    id: int
    company: str
    title: str

    class Config:
        orm_mode = True


class SkillsBase(BaseModel):
    skill: str
    subcategory: str | None = None
    proficiency: str | None = None


class SkillsCreate(SkillsBase):
    pass


class Skills(SkillsBase):
    id: int
    skill: str

    class Config:
        orm_mode = True


class ProjectsBase(BaseModel):
    title: str
    description: str | None = None


class ProjectsCreate(ProjectsBase):
    pass


class Projects(ProjectsBase):
    id: int
    title: str

    class Config:
        orm_mode = True


class CertificationsBase(BaseModel):
    title: str
    description: str | None = None
    date: datetime | None = None
    link: str | None = None


class CertificationsCreate(CertificationsBase):
    pass


class Certifications(CertificationsBase):
    id: int
    title: str

    class Config:
        orm_mode = True


class HonorsAndAwardsBase(BaseModel):
    title: str
    description: str | None = None


class HonorsAndAwardsCreate(HonorsAndAwardsBase):
    pass


class HonorsAndAwards(HonorsAndAwardsBase):
    id: int
    title: str

    class Config:
        orm_mode = True


class InterestsBase(BaseModel):
    interest: str
    description: str | None = None
    subcategory: str | None = None


class InterestsCreate(InterestsBase):
    pass


class Interests(InterestsBase):
    id: int
    interest: str

    class Config:
        orm_mode = True
