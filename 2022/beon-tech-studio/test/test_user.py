import json
from datetime import datetime

from pytest import fixture
from unittest import mock

from user import (
    User,
    _calculate_age_from_today,
    _filter_users)

ALL_USERS_FILE_PATH = 'test/users.json'
FILTERED_USERS_FILE_PATH = 'test/users_filtered.json'

from icecream import ic


@fixture
def all_users_fixture():
    with open(ALL_USERS_FILE_PATH) as file:
        return json.load(file)


@fixture
def filtered_users():
    with open(FILTERED_USERS_FILE_PATH) as file:
        return json.load(file)


class TestUser:
    def test_get_all_ok(self):
        users = User.get_all(ALL_USERS_FILE_PATH)
        ic(users)
        with open(FILTERED_USERS_FILE_PATH) as file:
            filtered_users = json.load(file)
            user = filtered_users[0]
            user['age'] = 31
            assert json.load(file) == users


@mock.patch('user.datetime')
def test__calculate_age_31_from_today(mock_datetime):
    fake_today = '2022-09-15'
    mock_datetime.today.return_value = datetime.strptime(fake_today, '%Y-%M-%d')
    mock_datetime.strptime = datetime.strptime

    birth_date = '1991-09-15'
    assert _calculate_age_from_today(birth_date) == 31


@mock.patch('user.datetime')
def test__calculate_age_30_from_today(mock_datetime):
    fake_today = '2022-09-15'
    mock_datetime.today.return_value = datetime.strptime(fake_today, '%Y-%M-%d')
    mock_datetime.strptime = datetime.strptime

    birth_date = '1991-09-15'
    assert _calculate_age_from_today(birth_date) == 31


def test__filter_users_ok(all_users_fixture, filtered_users):
    assert _filter_users(all_users_fixture) == filtered_users
