import os 
from sqlmodel import create_engine, SQLModel, Session
import sqlmodel


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}?check_same_thread=False"
engine = create_engine(sqlite_url, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session