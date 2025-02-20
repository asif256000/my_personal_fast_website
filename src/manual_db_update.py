from pprint import pprint

from data import db_ops
from data.db_init import get_db


def manual_add_db_entries(commands: list[dict]):
    for cmds in commands:
        db = next(get_db())
        table = cmds["table"]
        data = cmds["data"]  # e.g. {"title": "Something new"}
        data["fk_user"] = 1
        print(f"Adding data for {table=} with {data=}")
        db_ops.add_data_to_table(db, table_name=table, data=data)
        db.close()


def manual_update_db_entries(commands: list[dict]):
    for cmds in commands:
        db = next(get_db())
        table = cmds["table"]
        updated_data = cmds["updated_data"]  # e.g. {"title": "Something new"}
        # filter_data = cmds["filter_data"] # e.g. {"title": "What was there before", "fk_user": 1}
        # filtered_data = db_ops.filter_data_from_table(db, table, lookup_filter=filter_data)[0]
        filtered_data = db_ops.filter_data_with_id(db, table, lookup_id=cmds["lookup_id"])
        print(f"Updating data for {table=} for id={filtered_data.id}. {updated_data=}")
        db_ops.update_data_with_id(db, table_name=table, lookup_id=filtered_data.id, data=updated_data)
        db.close()


def manual_delete_db_entries(commands: list[dict]):
    for cmds in commands:
        db = next(get_db())
        table = cmds["table"]
        id = cmds["id"]
        deleted_record = db_ops.delete_data_by_id(db=db, table_name=table, lookup_id=id)
        print(f"Deleted {deleted_record}")
        db.close()


def manual_read_db_entries(reqd_tables: list[str] = None):
    db = next(get_db())
    if not reqd_tables:
        reqd_tables = [
            "basic_info",
            "education",
            "experience",
            "skills",
            "projects",
            "certifications",
            "honors_and_awards",
            "interests",
            "resume",
        ]
    for table_name in reqd_tables:
        for entry in db_ops.read_data_from_table(db, table_name):
            print(f"{table_name=}")
            pprint(vars(entry))
    db.close()


if __name__ == "__main__":
    add_commands = [{"table": "", "data": {}}]
    manual_add_db_entries(add_commands)
    update_commands = [{}]
    # manual_update_db_entries(update_commands)
    delete_commands = [{}]
    # manual_delete_db_entries(delete_commands)
    manual_read_db_entries(reqd_tables=["basic_info"])
