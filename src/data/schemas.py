from datetime import date

from pydantic import BaseModel


class BasicInfoBase(BaseModel):
    name: str
    email: str


class BasicInfoCreate(BasicInfoBase):
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
    duration_start: date
    duration_end: date | None = None
    major: str | None = None
    fk_user: int


class EducationCreate(EducationBase):
    institution_logo: str | None = None
    institution_link: str | None = None
    location: str | None = None
    minor: str | None = None
    gpa: str | None = None
    courses: str | None = None
    important_links: dict | None = None


class Education(EducationBase):
    id: int

    class Config:
        from_attributes = True


class ExperienceBase(BaseModel):
    company: str
    title: str
    location: str | None = None
    duration_start: date
    duration_end: date | None = None
    tech_stack: str | None = None
    fk_user: int


class ExperienceCreate(ExperienceBase):
    company_logo: str | None = None
    company_link: str | None = None
    description: list | None = None
    important_links: dict | None = None


class Experience(ExperienceBase):
    id: int

    class Config:
        from_attributes = True


class SkillsBase(BaseModel):
    skill: str
    fk_user: int


class SkillsCreate(SkillsBase):
    subcategory: str | None = None
    proficiency: str | None = None


class Skills(SkillsBase):
    id: int

    class Config:
        from_attributes = True


class ProjectsBase(BaseModel):
    title: str
    fk_user: int


class ProjectsCreate(ProjectsBase):
    description: str | None = None
    link: str | None = None


class Projects(ProjectsBase):
    id: int

    class Config:
        from_attributes = True


class CertificationsBase(BaseModel):
    title: str
    issuer: str
    link: str | None = None
    fk_user: int


class CertificationsCreate(CertificationsBase):
    description: str | None = None
    achievement_date: date | None = None


class Certifications(CertificationsBase):
    id: int

    class Config:
        from_attributes = True


class HonorsAndAwardsBase(BaseModel):
    title: str
    fk_user: int


class HonorsAndAwardsCreate(HonorsAndAwardsBase):
    description: str | None = None


class HonorsAndAwards(HonorsAndAwardsBase):
    id: int

    class Config:
        from_attributes = True


class InterestsBase(BaseModel):
    interest: str
    fk_user: int


class InterestsCreate(InterestsBase):
    subcategory: str | None = None


class Interests(InterestsBase):
    id: int

    class Config:
        from_attributes = True


class ResumeBase(BaseModel):
    file_path: str
    is_latest: bool
    fk_user: int


class ResumeCreate(ResumeBase):
    pass


class Resume(ResumeBase):
    id: int

    class Config:
        from_attributes = True
