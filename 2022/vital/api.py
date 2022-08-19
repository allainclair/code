from logging import getLogger

from dotenv import load_dotenv
from fastapi import (
    FastAPI,
    HTTPException,
)

from config import (
    email,
    password,
)
from dateutils import (
    add_days_to_date,
    date_day_generator,
)
from exception_detail import (
    MALFORMED_START_OR_END_DATE,
    NO_AVAILABLE_DATA,
)
from libreview_service import LibreViewService

# Shift days to zip a pair of next days.
SHIFT_DAYS = 2

logger = getLogger(__name__)
load_dotenv()
app = FastAPI()


@app.get('/glucose')
def get_glucose(start_date: str, end_date: str):
    start_dates = date_day_generator(start_date, end_date)
    if not start_dates:
        raise HTTPException(*MALFORMED_START_OR_END_DATE)

    shifted_start = add_days_to_date(start_date, SHIFT_DAYS)
    shifted_end = add_days_to_date(end_date, SHIFT_DAYS)
    end_dates = date_day_generator(shifted_start, shifted_end)

    patients_glucose = LibreViewService.getall(
        email, password, start_dates, end_dates)

    if not patients_glucose:
        raise HTTPException(*NO_AVAILABLE_DATA)

    return {'data': patients_glucose}
