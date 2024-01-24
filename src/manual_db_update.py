from pprint import pprint

from data import db_ops
from web.routes import get_db


def manual_update_db_entries():
    db = next(get_db())
    table = "education"
    filter_data = {"institution": "Virginia Tech", "fk_user": 1}
    updated_data = {
        "major": "Computer Science and Applications",
        "gpa": "3.85 out of 4",
        "courses": "Information Visualization, Fundamentals of Information Security, Applications of Machine Learning, Theory of Algorithms, Data Analysis, Computer Vision, Natural Language Processing, AI for Software Delivery",
    }
    filtered_data = db_ops.filter_data_from_table(db, table, filter_data)
    print(f"Updating data for {table=} for {filter_data=}. {updated_data=}")
    db_ops.update_data_with_id(
        db, table_name="education", lookup_id=filtered_data[0].id, data={"degree": "Master of Engineering"}
    )
    db.close()

    db = next(get_db())
    filter_data = {"institution": "Vellore Institute of Technology (VIT), Vellore", "fk_user": 1}
    updated_data = {"major": "Computer Science and Engineering"}
    filtered_data = db_ops.filter_data_from_table(db, table, filter_data)
    print(f"Updating data for {table=} for {filter_data=}. {updated_data=}")
    db_ops.update_data_with_id(
        db, table_name="education", lookup_id=filtered_data[0].id, data={"degree": "Master of Engineering"}
    )
    db.close()


def manual_read_db_entries():
    db = next(get_db())
    for entry in db_ops.read_data_from_table(db, "basic_info"):
        pprint(vars(entry))
    for entry in db_ops.read_data_from_table(db, "education"):
        pprint(vars(entry))
    for entry in db_ops.read_data_from_table(db, "experience"):
        pprint(vars(entry))
    for entry in db_ops.read_data_from_table(db, "skills"):
        pprint(vars(entry))
    for entry in db_ops.read_data_from_table(db, "projects"):
        pprint(vars(entry))
    for entry in db_ops.read_data_from_table(db, "certifications"):
        pprint(vars(entry))
    for entry in db_ops.read_data_from_table(db, "honors_and_awards"):
        pprint(vars(entry))
    for entry in db_ops.read_data_from_table(db, "interests"):
        pprint(vars(entry))
    for entry in db_ops.read_data_from_table(db, "resume"):
        pprint(vars(entry))
    db.close()


if __name__ == "__main__":
    manual_update_db_entries()
    manual_read_db_entries()
