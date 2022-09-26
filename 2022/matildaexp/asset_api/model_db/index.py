from sqlmodel import (
    Field,
    SQLModel)


class Index(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    value: float

    @property
    def saved(self):
        return self.id is not None
