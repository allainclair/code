"""Given a number, insert '-' between two consecutive odd numbers
and '*' between consecutive even numbers. Ignore the 0 number Ex:

insert_chars(11220334566)
'1-12*203-3456*6'
"""


def both_numbers_are_even(number_1, number_2):
    return is_even(number_1) and is_even(number_2)


def both_numbers_are_odd(number_1, number_2):
    return not is_even(number_1) and not is_even(number_2)


def is_even(number):
    return number % 2 == 0


def insert_chars(number):
    digits = str(number)
    aux = []
    for digit_1, digit_2 in zip(digits[:-1], digits[1:]):
        if '0' in {digit_1, digit_2}:
            digits = digit_1
        elif both_numbers_are_even(int(digit_1), int(digit_2)):
            digits = digit_1 + '*'
        elif both_numbers_are_odd(int(digit_1), int(digit_2)):
            digits = digit_1 + '-'
        else:
            digits = digit_1
        aux.append(digits)
    aux.append(digit_2)

    return ''.join(aux)


def main():
    assert insert_chars(11220334566) == '1-12*203-3456*6'


def test_is_even():
    assert is_even(2)
    assert not is_even(3)
    assert is_even(4)
    assert not is_even(5)


if __name__ == '__main__':
    main()
