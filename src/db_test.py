import sqlite3

conn = sqlite3.connect("profile.db")
cursor = conn.cursor()


def read_data_from_db(table_name):
    print(f"Reading data from table: {table_name}")
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    print("\n")


read_data_from_db("basic_info")
read_data_from_db("education")
read_data_from_db("experience")
read_data_from_db("skills")
read_data_from_db("projects")
read_data_from_db("certifications")
read_data_from_db("honors_and_awards")
read_data_from_db("interests")
read_data_from_db("resume")
