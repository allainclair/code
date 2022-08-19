from datetime import (
    datetime,
    timedelta,
)
from logging import getLogger

DATE_FORMAT = '%Y-%m-%d'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

MINUTE = 60
HOUR = 60
DAY = 24

logger = getLogger(__name__)


def add_days_to_date(date, days):
    date_object = datetime.strptime(date, DATE_FORMAT)
    date_object = date_object + timedelta(days=days)
    return date_object.strftime(DATE_FORMAT)


def date_to_timestamp(date):
    try:
        return int(datetime.strptime(date, DATE_FORMAT).timestamp())
    except ValueError as e:
        logger.exception(e)


def timestamp_to_date(timestamp, fmt=DATETIME_FORMAT):
    return datetime.fromtimestamp(timestamp).strftime(fmt)


def start_end_date_to_from_and_days_ago(start_date, end_date):
    start_timestamp = date_to_timestamp(start_date)
    end_timestamp = date_to_timestamp(end_date)
    if _validate_timestamp_interval(start_timestamp, end_timestamp):
        return start_end_timestamp_to_from_and_days_ago(start_timestamp, end_timestamp)

    return False


def start_end_timestamp_to_from_and_days_ago(start_in_timestamp, end_in_timestamp):
    difference = end_in_timestamp - start_in_timestamp
    return end_in_timestamp, int(difference/(MINUTE*HOUR*DAY))


def date_day_generator(start, end, fmt=DATE_FORMAT):
    start, end = date_to_timestamp(start), date_to_timestamp(end)
    if _validate_timestamp_interval(start, end):
        dates = []
        for time in range(start, end, 1*MINUTE*HOUR*DAY):
            dates.append(time)
        dates.append(end)
        return [timestamp_to_date(date, fmt) for date in dates]

    return False


def _validate_timestamp_interval(start_timestamp, end_timestamp):
    return (
        None not in {start_timestamp, end_timestamp}
        and start_timestamp < end_timestamp)
