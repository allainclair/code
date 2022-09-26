from sqlmodel import create_engine, SQLModel, Session


def start(path_db='database.db'):
    path = f'sqlite:///{path_db}'
    eng = create_engine(path)
    SQLModel.metadata.create_all(eng)
    return eng
