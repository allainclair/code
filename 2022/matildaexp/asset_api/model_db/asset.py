from sqlmodel import (
    Field,
    SQLModel)


class Asset(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    ir: float
    fix_interest: float
    duration: int  # Years
    id_index: int  # TODO: Add foreign key.

    @property
    def saved(self):
        return self.id is not None
