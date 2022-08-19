from datetime import datetime

from dateutils import (
    DATE_FORMAT,
    add_days_to_date,
    date_to_timestamp,
    start_end_date_to_from_and_days_ago,
    start_end_timestamp_to_from_and_days_ago,
)


def test_add_days_to_date():
    date = '2022-08-30'
    added_date = '2022-09-01'
    assert add_days_to_date(date, 2) == added_date


def test_date_to_timestamp():
    date = '2022-01-01'
    timestamp = date_to_timestamp(date)
    assert datetime.fromtimestamp(timestamp) == datetime.strptime(date, DATE_FORMAT)


def test_start_end_date_to_from_and_days_behind():
    start_date, end_date = '2022-01-01', '2022-02-01'
    end_in_timestamp = date_to_timestamp(end_date)

    from_, days = start_end_date_to_from_and_days_ago(start_date, end_date)
    assert from_ == end_in_timestamp
    assert days == 31


def test_start_end_timestamp_to_from_and_days_behind():
    start_date, end_date = '2022-01-01', '2022-02-01'
    start_in_timestamp = date_to_timestamp(start_date)
    end_in_timestamp = date_to_timestamp(end_date)

    from_, days = start_end_timestamp_to_from_and_days_ago(
        start_in_timestamp, end_in_timestamp)
    assert from_ == end_in_timestamp
    assert days == 31

