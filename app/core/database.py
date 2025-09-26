from sqlmodel import Session, create_engine
from typing import Annotated
from fastapi import Depends

sqlite_file = "database.db"
sqlite_url = f"sqlite:///{sqlite_file}"
connect_args = {"check_same_thread": False}  # only for SQLite, needed for multithreading
engine = create_engine(sqlite_url, connect_args=connect_args)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]