from datetime import datetime

from marshmallow import (
    Schema,
    fields)

USER_DATA_PATH = 'data/users.json'

from icecream import ic


class UserSchema(Schema):
    id = fields.Int()
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Str(load_default=None)
    gender = fields.Str(load_default=None)
    ip_address = fields.Str()
    birth_date = fields.Str(load_default=None)
    age = fields.Method('get_age')

    def get_age(self, obj):
        birth_date = datetime.strptime(obj['birth_date'], '%Y-%M-%d')
        today = datetime.today()
        return today.year - birth_date.year - (
                (today.month, today.day) < (birth_date.month, birth_date.day))


class User:
    @classmethod
    def get_all(cls, user_data_path=USER_DATA_PATH):
        user_schema = UserSchema(many=True)
        with open(user_data_path) as file:
            users = user_schema.loads(file.read())
            users = _filter_users(users)
            return user_schema.dump(users)


def _calculate_age_from_today(birth_date):
    birth_date = datetime.strptime(birth_date, '%Y-%M-%d')
    today = datetime.today()
    return today.year - birth_date.year - (
                (today.month, today.day) < (birth_date.month, birth_date.day))


def _filter_users(users):
    return [
        user  # Filter out users without email or birth_date or gender.
        for user in users if user['email'] and user['gender'] and user['birth_date']
    ]
