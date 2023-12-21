import os

import databases
from dotenv import load_dotenv
from graphviz import Digraph
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")
database = databases.Database(DATABASE_URL)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# session = Session(engine)
# graph = Digraph(comment="Profile Graph")

Base = declarative_base()
# Base = automap_base()
# Base.prepare(engine, reflect=True)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# # Iterate over the tables in the database schema
# for table in Base.classes:
#     # Add the table to the graph
#     graph.node(table.__tablename__, label=table.__tablename__)

#     # Iterate over the relationships for the table
#     for relationship in table.__mapper__.relationships:
#         # Add the relationship to the graph
#         graph.edge(table.__tablename__, relationship.mapper.class_.__tablename__)

# # Render the graph
# graph.render("mydatabase_graph")
