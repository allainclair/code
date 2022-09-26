from pydantic import BaseModel


class Asset(BaseModel):
    name: str
    ir: float
    fix_interest: float
    duration: int  # Years
    indexed: int
    id: int | None = None
