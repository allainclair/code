"""Merge namedtuple records into a single one."""
from collections import namedtuple


def merge(*records):
    tuple_dict = {}
    for record in records:
        tuple_dict = {**tuple_dict, **record._asdict()}

    Patient = namedtuple('Patient', tuple_dict.keys())
    patient = Patient(*tuple_dict.values())
    return patient


def main():
    PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
    personal_details = PersonalDetails(date_of_birth='06-04-1972')

    Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
    complexion = Complexion(eye_color='Blue', hair_color='Black')

    print(merge(personal_details, complexion))


if __name__ == '__main__':
    main()


