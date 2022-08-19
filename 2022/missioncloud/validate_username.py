"""Validate a username given the rules:
1. Size >= 4
2. Must start with ascii_letters
3. Can not have last char == '_'
4. Contains no or a single underscore
5. Must have only ascii_letters or numbers
"""
import string


def validate(username):
    minimum_size = len(username) >= 4
    start_with_char = username[0] in string.ascii_letters
    last_char_is_not_underscore = username[-1] != '_'
    contains_no_or_a_single_underscore = username.count('_') <= 1
    is_valid = {
        minimum_size,
        start_with_char,
        last_char_is_not_underscore,
        contains_no_or_a_single_underscore,
    }

    if not all(is_valid):
        return False

    allowed_chars = set(string.ascii_letters + string.digits + '_')
    return all(True if char in allowed_chars else False for char in username)


def main():
    assert validate("Mike_Standish")
    assert not validate("Mike Standish")
    assert validate("Mike_1Standish1")
    assert not validate("1Mike_1Standish1")
    assert not validate("M_i_ke01St_andish1")


if __name__ == '__main__':
    main()
