from sqlmodel import (
    SQLModel,
    create_engine)


def get_db_path(path_file):
    return f'sqlite:///{path_file}'


def start(path_db):
    path = get_db_path(path_db)
    eng = create_engine(path)
    SQLModel.metadata.create_all(eng)
    return eng
