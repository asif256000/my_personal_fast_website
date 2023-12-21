from datetime import date

from sqlalchemy.orm import Session

from data import db_init, models, schemas

BASIC_DETAILS = {
    "name": "Asif Iqbal Rahaman",
    "email": "asif256000+job@gmail.com",
    "phone": "+1 (336) 223-2730",
    "location": "Blacksburg, VA",
    "website": "https://asifiqbal.xyz",
    "linkedin": "https://www.linkedin.com/in/asif-iqbal-r/",
    "github": "https://www.github.com/asif256000",
}
EDUCATIONS = [
    {
        "institution": "Virginia Tech",
        "location": "Blacksburg, VA",
        "duration_start": date(2022, 8, 15),
        "duration_end": date(2024, 5, 20),
        "degree": "Master of Science",
        "major": "Computer Science",
        "minor": "Data Analysis and AI",
        "gpa": "3.8",
        "courses": "Information Visualization, Fundamentals of Information Security, Applications of Machine Learning, Theory of Algorithms, Data Analytics, Computer Vision, Natural Language Processing, AI for Software Delivery",
    },
    {
        "institution": "Vellore Institute of Technology (VIT), Vellore",
        "location": "Vellore, India",
        "duration_start": date(2015, 7, 11),
        "duration_end": date(2019, 5, 22),
        "degree": "Bachelor of Technology",
        "major": "Computer Science",
        "minor": "Bioinformatics",
        "gpa": "7.92",
        "courses": "Data Structures and Algorithms, Object Oriented Programming, Database Management Systems, Operating Systems, Network Architecture, Software Engineering, Data Mining, Machine Learning, Deep Learning, Computer Vision, Cyber Security, Internet of Things",
    },
]
EXPERIENCES = [
    {
        "company": "Virginia Tech - Department of Computational Cell Biology",
        "location": "Blacksburg, VA",
        "title": "Student Data Analyst",
        "duration_start": date(2022, 10, 10),
        "description": """
        - Problem Statement: Simulate Cell Cycle with boolean model of cell interactions.
        - Current work: Analyze the simulation results for all perturbations of the model and identify the perturbations that hinder or improve the cell cycle.
        - Preprint available: https://www.biorxiv.org/content/10.1101/2023.10.30.564745v1
        - Future plans: Implementing a better scoring mechanism, optimizing the method to run larger models, and applying the method on models of cancerous cells to identify potential drug targets.
        """,
    },
    {
        "company": "Seclore Technology Pvt. Ltd.",
        "location": "Mumbai, India",
        "title": "Product Engineer",
        "duration_start": date(2021, 12, 6),
        "duration_end": date(2022, 7, 15),
        "description": """
        - Cloud automation: Developed DevOps automation that was able to deploy complete product for a client in less than an hour in a fully managed and scalable AWS architecture. This decreased customer onboarding time from several days to few hours.
        - Customer Infra Stack Codification: Implemented individual customer infrastructure as a AWS Cloudformation stack via aws-cdk and pynamodb modules in Python.
        - Collaboration: Team of 3 worked with Subversion in an agile environment to develop the cloud automation.
        """,
    },
    {
        "company": "Ericsson Global India Pvt. Ltd.",
        "location": "Bangalore, India",
        "title": "Software Developer",
        "duration_start": date(2019, 1, 14),
        "duration_end": date(2021, 7, 26),
        "description": """
        - Surface Automation Framework: Worked on development of custom RPA framework that helped automate various network management tools. Automation gain with RPA framework reached 35% per month.
        - Rule-based Data Analysis Engine: Developed rule-based recommendation and data analysis engine that calculates lists of high-impact network cells. The data analysis engine worked on large network data (10M rows and 5K cols, approx 30GB parquet file) on a daily basis for about 20 clients in less than 4 hours with a few parallel processing.
        - Impact: With the rule-based recommendation & root cause analysis system automation gain reached 36% per month.
        - Other projects: Integrated the custom RPA framework with existing automation platform. Also developed a system to fetch large amount of network data to local system via API, cleaned them and stored them as parquet files.
        """,
    },
]
SKILLS = {
    "Programming Language": {
        "Advanced": ["Python", "Rust"],
        "Intermediate": ["JavaScript", "HTML", "SQL", "Bash", "C++"],
        "Beginner": ["Java", "R"],
    },
    "Frameworks": {
        "Advanced": [
            "FastAPI",
            "Flask",
            "Pandas",
            "NumPy",
            "PyTorch",
            "Matplotlib",
            "Seaborn",
            "Scikit-Learn",
            "OpenCV",
            "Win32",
            "PyAutoGUI",
            "Pillow",
            "AWS-CDK",
        ],
        "Intermediate": ["Vue.js", "Apache Airflow"],
    },
    "Tools": {
        "Advanced": ["Git", "Postman", "Jupyter Notebook", "MongoDB", "MySQL", "SQLite", "RestAPI"],
        "Intermediate": ["Docker", "Subversion", "Jenkins", "Vim", "DynamoDB", "Parquet", "AWS CLI"],
    },
    "Platforms": {
        "Advanced": ["Linux", "Windows", "MacOS", "AWS"],
        "Intermediate": ["Heroku", "Arduino"],
        "Beginner": ["Azure", "Android", "iOS"],
    },
}
PROJECTS = [
    {
        "title": "Portfolio Website",
        "description": "This website is a portfolio website that I made using FastAPI and Vue.js.",
        "link": "https://asifiqbal.xyz",
    },
    {
        "title": "EEG-to-Text with Sentiment Analysis",
        "description": "This is a class project for Natural Language Processing course. The goal of this project is to convert EEG signals to text along with performing zero-shot sentiment analysis on the signal.",
        "link": "https://github.com/asif256000/EEG-to-Text-Project",
    },
    {
        "title": "Multi-Object Tracking using GAN with FairMOT",
        "description": "This is a class project for Computer Vision course. The goal of this project is to implement a GAN based object tracker using FairMOT base architecture.",
        "link": "https://github.com/stevend-15/cv-project-fall23",
    },
]
CERTIFICATES = [
    {
        "title": "Python for Data Science and Machine Learning Bootcamp",
        "issuer": "Udemy",
        "description": "Learned how to use NumPy, Pandas, Seaborn, Matplotlib, Plotly, Scikit-Learn, Machine Learning, Tensorflow, etc with respect to ML Projects.",
        "achievement_date": date(2021, 5, 6),
        "link": "https://www.udemy.com/certificate/UC-a739cf18-dc7c-43fd-8450-ee1038e0aa5a/",
    },
    {
        "title": "Neural Networks and Deep Learning",
        "issuer": "Coursera",
        "description": "Learned how to build Shallow and Deep Neural Networks using Scikit-learn and PyTorch.",
        "achievement_date": date(2020, 1, 16),
        "link": "https://coursera.org/share/a2f4a958ffc2373aa4e369d1a9e00f72",
    },
    {
        "title": "Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization",
        "issuer": "Coursera",
        "description": "Learned how to improve Deep Neural Networks using regularization, dropout, batch normalization, etc. Dove deep into the black box of deep learning to understand how and why it works so well.",
        "achievement_date": date(2020, 7, 15),
        "link": "https://coursera.org/share/6def92a2dbb6e985b94b34e26f0868ae",
    },
]
HONORS_AWARDS = [
    {
        "title": "Ericsson Global India Pvt. Ltd. - bi-annual Galactic Award 2020",
        "description": "Awarded for the development of the rule-based recommendation and root cause analysis system and thereby automating a huge part of repetitive tasks iin the organization.",
    }
]
INTERESTS = {
    "Work": [
        "Automation",
        "Cloud Technologies",
        "Data Analysis",
        "Intelligent Web and Software Development",
        "Machine Learning",
    ],
    "Reading": ["Technology related blogs", "Recent developments in Python, Rust and other languages and frameworks"],
    "Other Hobbies": ["Leisure Reading", "Photography", "Soccer", "Table Tennis"],
}
RESUME_DATA = {
    "file_path": "Asif's Resume.pdf",
    "is_latest": True,
}


def populate_my_info(db: Session):
    basic_data = schemas.BasicInfoCreate(**BASIC_DETAILS)
    basic_info = models.BasicInfo(**basic_data.model_dump())
    db.add(basic_info)
    db.commit()
    db.refresh(basic_info)

    for education in EDUCATIONS:
        education_data = schemas.EducationCreate(**education)
        education_info = models.Education(**education_data.model_dump(), fk_user=basic_info.id)
        db.add(education_info)
    db.commit()

    for experience in EXPERIENCES:
        experience_data = schemas.ExperienceCreate(**experience)
        experience_info = models.Experience(**experience_data.model_dump(), fk_user=basic_info.id)
        db.add(experience_info)
    db.commit()

    for skill_category, skills in SKILLS.items():
        for skill_proficiency, skills_list in skills.items():
            for skill in skills_list:
                skill_data = schemas.SkillsCreate(
                    skill=skill, subcategory=skill_category, proficiency=skill_proficiency
                )
                skill_info = models.Skills(**skill_data.model_dump(), fk_user=basic_info.id)
                db.add(skill_info)
    db.commit()

    for project in PROJECTS:
        project_data = schemas.ProjectsCreate(**project)
        project_info = models.Projects(**project_data.model_dump(), fk_user=basic_info.id)
        db.add(project_info)
    db.commit()

    for certificate in CERTIFICATES:
        certificate_data = schemas.CertificationsCreate(**certificate)
        certificate_info = models.Certifications(**certificate_data.model_dump(), fk_user=basic_info.id)
        db.add(certificate_info)
    db.commit()

    for honor_award in HONORS_AWARDS:
        honor_award_data = schemas.HonorsAndAwardsCreate(**honor_award)
        honor_award_info = models.HonorsAndAwards(**honor_award_data.model_dump(), fk_user=basic_info.id)
        db.add(honor_award_info)
    db.commit()

    for interest_category, interests in INTERESTS.items():
        for interest in interests:
            interest_data = schemas.InterestsCreate(interest=interest, subcategory=interest_category)
            interest_info = models.Interests(**interest_data.model_dump(), fk_user=basic_info.id)
            db.add(interest_info)
    db.commit()

    resume_data = schemas.ResumeCreate(**RESUME_DATA)
    resume_info = models.Resume(**resume_data.model_dump(), fk_user=basic_info.id)
    db.add(resume_info)
    db.commit()


if __name__ == "__main__":
    # Create the database tables
    from data.db_init import Base

    Base.metadata.create_all(bind=db_init.engine)

    # Create a new session
    db = db_init.SessionLocal()

    try:
        populate_my_info(db)
        print("Data successfully added to the database.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()
