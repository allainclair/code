from pydantic import BaseModel


class Index(BaseModel):
    name: str
    value: float
    id: int | None = None
