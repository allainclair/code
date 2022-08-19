from fastapi.testclient import TestClient

from api import app
from exception_detail import (
    MALFORMED_START_OR_END_DATE,
    NO_AVAILABLE_DATA,
)

client = TestClient(app)


# TODO: mock the server.

def test_get_glucose():
    # Test needs 'pytest -s' to input the email code.
    start, end = '2022-04-20', '2022-04-25'
    response = client.get(f'/glucose?start_date={start}&end_date={end}')

    assert response.status_code == 200
    assert response.json()['data']


def test_get_glucose_malformed_start_date():
    start, end = '', '2022-04-25'
    response = client.get(f'/glucose?start_date={start}&end_date={end}')
    assert response.status_code == MALFORMED_START_OR_END_DATE.status_code
    assert response.json()['detail'] == MALFORMED_START_OR_END_DATE.detail


def test_get_glucose_malformed_end_date():
    start, end = '2022-04-20', ''
    response = client.get(f'/glucose?start_date={start}&end_date={end}')
    assert response.status_code == MALFORMED_START_OR_END_DATE.status_code
    assert response.json()['detail'] == MALFORMED_START_OR_END_DATE.detail


def test_get_glucose_bad_date_interval():
    start, end = '2022-04-25', '2022-04-20'  # end < start
    response = client.get(f'/glucose?start_date={start}&end_date={end}')
    assert response.status_code == MALFORMED_START_OR_END_DATE.status_code
    assert response.json()['detail'] == MALFORMED_START_OR_END_DATE.detail


def test_get_glucose_no_available_data():
    # Test needs 'pytest -s' to input the email code.
    start, end = '2022-03-01', '2022-03-02'
    response = client.get(f'/glucose?start_date={start}&end_date={end}')
    assert response.status_code == NO_AVAILABLE_DATA.status_code
    assert response.json()['detail'] == NO_AVAILABLE_DATA.detail
