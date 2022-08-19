from datetime import datetime

from pydantic import BaseModel


class GlucoseModel(BaseModel):
    glucose_average: float
    glucose_max: float
    date_start: datetime
    date_end: datetime
    patient_id: str

