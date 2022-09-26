from sqlmodel import (
    Field,
    SQLModel)


class StringModel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    string: str = Field(unique=True)
    object: str
