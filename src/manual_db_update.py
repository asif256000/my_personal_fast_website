from pprint import pprint

from data import db_ops
from data.db_init import get_db


def manual_add_db_entries(commands: list[dict]):
    for cmds in commands:
        db = next(get_db())
        table = cmds["table"]
        data = cmds["data"]  # e.g. {"title": "Something new"}
        data["fk_user"] = cmds.get("user_id", 1)
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
        if table_name == "skills":
            skills_data = db_ops.read_data_from_table(db, table_name)
            # Group skills by user
            skills_by_user = {}
            for skill in skills_data:
                user_id = skill.fk_user
                if user_id not in skills_by_user:
                    skills_by_user[user_id] = {}

                # Group by subcategory within each user
                subcategory = skill.subcategory
                if subcategory not in skills_by_user[user_id]:
                    skills_by_user[user_id][subcategory] = {}

                # Group by proficiency within each subcategory
                proficiency = skill.proficiency
                if proficiency not in skills_by_user[user_id][subcategory]:
                    skills_by_user[user_id][subcategory][proficiency] = []

                skills_by_user[user_id][subcategory][proficiency].append(skill)

            # Display the grouped skills
            print(f"\n{table_name}=")
            for user_id, subcategories in skills_by_user.items():
                print(f"User ID: {user_id}")
                for subcategory, proficiencies in subcategories.items():
                    print(f"Subcategory: {subcategory}")
                    for proficiency, skills in proficiencies.items():
                        print(f"  Proficiency: {proficiency}")
                        curr_skills = ", ".join([skill.skill for skill in skills])
                        print(f"    - {curr_skills}")
    db.close()


if __name__ == "__main__":
    add_commands = [{"table": "", "user_id": 0, "data": {}}]
    # manual_add_db_entries(add_commands)
    update_commands = [{}]
    # manual_update_db_entries(update_commands)
    delete_commands = [{}]
    # manual_delete_db_entries(delete_commands)
    manual_read_db_entries(reqd_tables=["projects"])
