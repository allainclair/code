from logging import getLogger

from requests import (
    get, post
)

import config
from dateutils import (
    start_end_date_to_from_and_days_ago,
    timestamp_to_date,
)
from glucose_model import GlucoseModel


URL_AUTH_LOGIN = 'https://api-eu.libreview.io/auth/login'
URL_AUTH_SEND_CODE = 'https://api-eu.libreview.io/auth/continue/2fa/sendcode'
URL_AUTH_RESULT = 'https://api-eu.libreview.io/auth/continue/2fa/result'

URL_DASHBOARD = 'https://api-eu.libreview.io/dashboard'

URL_PATIENTS = 'https://api-eu.libreview.io/patients/'
# We need to pass the captcha to use this URL.
# URL_PATIENTS_EXPORT = 'https://api-eu.libreview.io/patients/{}/export'

NUM_PERIODS = 1
PATIENTS_PARAMS = f'glucoseHistory?from={{}}&numPeriods={NUM_PERIODS}&period={{}}'

# Shift days to pair two days in a row.
SHIFT_DAYS = 2

logger = getLogger(__name__)

dashhboard_payload = {
    "filters": [],
    "columns": [],
    "interval": "14",
    "view": "Dashboard.allPatients",
    "count": 50,
    "page": 1,
    "searching": {},
}


class LibreViewService:
    auth_ticket_token = None
    email = None
    password = None

    @classmethod
    def authenticate(cls, email=config.email, password=config.password):
        """Authenticate with login once and return auth_ticket_token"""
        cls.email, cls.password = email, password
        if cls.auth_ticket_token is not None:
            return cls.auth_ticket_token
        else:
            return cls.login()

    @classmethod
    def login(cls):
        token = _auth_login(cls.email, cls.password)
        token = _auth_send_code(token)

        # The unique manual step that we need.
        code = input('Email Code > ')

        cls.auth_ticket_token = _auth_result(code, token)
        return cls.auth_ticket_token

    @classmethod
    def getall(cls, email, password, start_dates, end_dates):
        headers = {'Authorization': f'Bearer {cls.authenticate(email, password)}'}
        all_patients_glucose = []
        for start_date, end_date in zip(start_dates, end_dates):
            patients_glucose = _get_patients_glucose(headers, start_date, end_date)
            if patients_glucose:
                all_patients_glucose += patients_glucose

        return all_patients_glucose


def _auth_login(email, password):
    credentials = {'email': email, 'password': password}
    json_object = _post_and_get_json(URL_AUTH_LOGIN, json=credentials)

    try:
        auth_ticket_token = json_object['data']['authTicket']['token']
    except KeyError:
        logger.exception('Login with credentials failed. No token will be returned')
        auth_ticket_token = None

    return auth_ticket_token


def _auth_result(code, token):
    payload = {'code': code, 'isPrimaryMethod': False}
    header = {'Authorization': f'Bearer {token}'}
    response = post(URL_AUTH_RESULT, headers=header, json=payload)

    try:
        auth_ticket_token = response.json()['data']['authTicket']['token']
    except KeyError:
        logger.exception('Auth result failed. No token will be returned')
        auth_ticket_token = None

    return auth_ticket_token


def _auth_send_code(token):
    payload = {'isPrimaryMethod': False}
    headers = {'Authorization': f'Bearer {token}'}
    json_object = _post_and_get_json(URL_AUTH_SEND_CODE, headers, payload)

    try:
        ticket_token = json_object['ticket']['token']
    except KeyError:
        logger.exception('Send code failed. No token will be returned')
        ticket_token = None

    return ticket_token


def _build_output(json_object, patient_id):
    try:
        periods = json_object['data']['periods']
        period = periods[0]
        data = period['data']
        date_start, date_end = period['dateStart'], period['dateEnd']
        date_start = timestamp_to_date(date_start)
        date_end = timestamp_to_date(date_end)
        return GlucoseModel(
            glucose_average=period['avgGlucose'],
            glucose_max=data['maxGlucoseValue'],
            date_start=date_start,
            date_end=date_end,
            patient_id=patient_id)
    except (KeyError, IndexError, TypeError):
        # We do not have data for some objects.
        logger.exception(f'Some data not available for {json_object}')


def _get_patients_glucose(headers, start, end):
    json_object = _post_and_get_json(URL_DASHBOARD, headers, dashhboard_payload)
    token = json_object['ticket']['token']
    patient_ids = [patient['id'] for patient in json_object['data']['results']]

    from_, days = start_end_date_to_from_and_days_ago(start, end)
    patients_glucose = []
    for patient_id in patient_ids:
        headers = {'Authorization': f'Bearer {token}'}

        params = PATIENTS_PARAMS.format(from_, days)
        url = f'{URL_PATIENTS}{patient_id}/{params}'
        response = get(url, headers=headers)
        json_object = response.json()

        patient_glucose = _build_output(json_object, patient_id)
        if patient_glucose is not None:
            patients_glucose.append(patient_glucose)

    return patients_glucose


def _post_and_get_json(url, headers=None, json=None):
    return post(url, headers=headers, json=json).json()
