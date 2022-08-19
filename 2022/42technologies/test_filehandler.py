from filehandler import (
    load, parse
)


def test_load():
    test_filepath = 'data-small-input.txt'
    rows = load(test_filepath)

    # Different way of getting the same result.
    with open(test_filepath) as file:
        test_rows = [row.strip().split('|') for row in file]
        assert rows == test_rows


def test_parse():
    row = ['property1', 'property2', 'property3', 'metric1', 'metric2']
    assert parse(row, 3, 2) == ([
        'property1', 'property2', 'property3'], ['metric1', 'metric2'])
