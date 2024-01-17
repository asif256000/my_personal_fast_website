from datetime import date

from pydantic import BaseModel


class BasicInfoBase(BaseModel):
    name: str


class BasicInfoCreate(BasicInfoBase):
    email: str
    phone: str | None = None
    location: str | None = None
    website: str | None = None
    linkedin: str | None = None
    github: str | None = None
    intro: str | None = None


class BasicInfo(BasicInfoBase):
    id: int

    class Config:
        from_attributes = True


class EducationBase(BaseModel):
    institution: str
    degree: str


class EducationCreate(EducationBase):
    institution_logo: str | None = None
    location: str | None = None
    duration_start: date
    duration_end: date | None = None
    major: str | None = None
    minor: str | None = None
    gpa: str | None = None
    courses: str | None = None


class Education(EducationBase):
    id: int
    fk_user: int

    class Config:
        from_attributes = True


class ExperienceBase(BaseModel):
    company: str
    title: str


class ExperienceCreate(ExperienceBase):
    company_logo: str | None = None
    location: str | None = None
    duration_start: date
    duration_end: date | None = None
    description: list | None = None


class Experience(ExperienceBase):
    id: int
    fk_user: int

    class Config:
        from_attributes = True


class SkillsBase(BaseModel):
    skill: str


class SkillsCreate(SkillsBase):
    subcategory: str | None = None
    proficiency: str | None = None


class Skills(SkillsBase):
    id: int
    fk_user: int

    class Config:
        from_attributes = True


class ProjectsBase(BaseModel):
    title: str


class ProjectsCreate(ProjectsBase):
    description: str | None = None
    link: str | None = None


class Projects(ProjectsBase):
    id: int
    fk_user: int

    class Config:
        from_attributes = True


class CertificationsBase(BaseModel):
    title: str
    issuer: str


class CertificationsCreate(CertificationsBase):
    description: str | None = None
    achievement_date: date | None = None
    link: str | None = None


class Certifications(CertificationsBase):
    id: int
    fk_user: int

    class Config:
        from_attributes = True


class HonorsAndAwardsBase(BaseModel):
    title: str


class HonorsAndAwardsCreate(HonorsAndAwardsBase):
    description: str | None = None


class HonorsAndAwards(HonorsAndAwardsBase):
    id: int
    fk_user: int

    class Config:
        from_attributes = True


class InterestsBase(BaseModel):
    interest: str


class InterestsCreate(InterestsBase):
    subcategory: str | None = None


class Interests(InterestsBase):
    id: int
    fk_user: int

    class Config:
        from_attributes = True


class ResumeBase(BaseModel):
    file_path: str


class ResumeCreate(ResumeBase):
    is_latest: bool


class Resume(ResumeBase):
    id: int
    fk_user: int

    class Config:
        from_attributes = True
