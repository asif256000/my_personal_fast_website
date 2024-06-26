from datetime import date
from pprint import pprint

from data import db_ops
from data.db_init import get_db


def manual_add_db_entries():
    db = next(get_db())
    table = "skills"
    data = {}
    print(f"Adding data for {table=} with {data=}")
    db_ops.add_data_to_table(db, table_name=table, data=data)
    db.close()


def manual_update_db_entries():
    db = next(get_db())
    table = "projects"
    updated_data = {}
    # filter_data = {"title": "EEG-to-Text with Sentiment Analysis", "fk_user": 1}
    # filtered_data = db_ops.filter_data_from_table(db, table, lookup_filter=filter_data)[0]
    filtered_data = db_ops.filter_data_with_id(db, table, lookup_id=1)
    print(f"Updating data for {table=} for id={filtered_data.id}. {updated_data=}")
    db_ops.update_data_with_id(db, table_name=table, lookup_id=filtered_data.id, data=updated_data)
    db.close()

    db = next(get_db())
    table = "projects"
    updated_data = {}
    # filter_data = {"title": "Multi-Object Tracking using GAN with FairMOT", "fk_user": 1}
    # filtered_data = db_ops.filter_data_from_table(db, table, lookup_filter=filter_data)[0]
    filtered_data = db_ops.filter_data_with_id(db, table, lookup_id=2)
    print(f"Updating data for {table=} for id={filtered_data.id}. {updated_data=}")
    db_ops.update_data_with_id(db, table_name=table, lookup_id=filtered_data.id, data=updated_data)
    db.close()

    db = next(get_db())
    table = "projects"
    updated_data = {}
    # filter_data = {"title": "Portfolio Website", "fk_user": 1}
    # filtered_data = db_ops.filter_data_from_table(db, table, lookup_filter=filter_data)[0]
    filtered_data = db_ops.filter_data_with_id(db, table, lookup_id=3)
    print(f"Updating data for {table=} for id={filtered_data.id}. {updated_data=}")
    db_ops.update_data_with_id(db, table_name=table, lookup_id=filtered_data.id, data=updated_data)
    db.close()


def manual_delete_db_entries():
    table = ""
    id_list = []
    for id in id_list:
        db = next(get_db())
        deleted_record = db_ops.delete_data_by_id(db=db, table_name=table, lookup_id=id)
        print(f"Deleted {deleted_record}")
        db.close()


def manual_read_db_entries():
    db = next(get_db())
    table_name = "basic_info"
    for entry in db_ops.read_data_from_table(db, table_name):
        print(f"{table_name=}")
        pprint(vars(entry))
    table_name = "education"
    for entry in db_ops.read_data_from_table(db, table_name):
        print(f"{table_name=}")
        pprint(vars(entry))
    table_name = "experience"
    for entry in db_ops.read_data_from_table(db, table_name):
        print(f"{table_name=}")
        pprint(vars(entry))
    table_name = "skills"
    for entry in db_ops.read_data_from_table(db, table_name):
        print(f"{table_name=}")
        pprint(vars(entry))
    table_name = "projects"
    for entry in db_ops.read_data_from_table(db, table_name):
        print(f"{table_name=}")
        pprint(vars(entry))
    table_name = "certifications"
    for entry in db_ops.read_data_from_table(db, table_name):
        print(f"{table_name=}")
        pprint(vars(entry))
    table_name = "honors_and_awards"
    for entry in db_ops.read_data_from_table(db, table_name):
        print(f"{table_name=}")
        pprint(vars(entry))
    table_name = "interests"
    for entry in db_ops.read_data_from_table(db, table_name):
        print(f"{table_name=}")
        pprint(vars(entry))
    table_name = "resume"
    for entry in db_ops.read_data_from_table(db, table_name):
        print(f"{table_name=}")
        pprint(vars(entry))
    db.close()


if __name__ == "__main__":
    # manual_add_db_entries()
    # manual_update_db_entries()
    # manual_delete_db_entries()
    manual_read_db_entries()
