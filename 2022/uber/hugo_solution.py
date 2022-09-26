"""Given a two-dimensional array of letters,
find a given word written in any of the 8 directions.
I.e.

EXAMPLE
Input: UBER

A  U  I  K  F  W  N
W  Q  B  O  L  X  P
T  L  A  E  R  E  S
Y  Z  X  E  R  L  W

Output: true
"""

"""

X  E  E  E  X
X  E  Z  E  X
X  E  E  E  X
X  X  X  X  E
word = 'ZEE'



Matriz n*n e w = n
Matriz:
Z  X  Z  X  Z  .  .  X
Z  X  Z  X  Z  .  .  X
Z  X  Z  X  Z  .  .  X
Z  X  Z  X  Z  .  .  X
Z  X  Z  X  Z  .  .  X
.  .  .  .  .  .  .  X
.  .  .  .  .  .  .  X
X  Z  X  Z  X  Z  X  Z  Apenas ultima linha diferente do padrão
word: 'ZZZZZZ..Z'

"""
from pprint import pp

from functools import partial


def main():
    # matrix = [
    #     ['A', 'U', 'I', 'K', 'F', 'W', 'N'],
    #     ['W', 'Q', 'B', 'O', 'L', 'X', 'P'],
    #     ['T', 'L', 'A', 'E', 'R', 'E', 'S'],
    #     ['Y', 'Z', 'X', 'E', 'R', 'L', 'W'],
    # ]
    # word = 'UBER'
    # print(hugo_solution(matrix, word))
    #
    # word = 'ZEE'
    # matrix = [
    #     ['X', 'E', 'E', 'E', 'X'],
    #     ['X', 'E', 'Z', 'E', 'X'],
    #     ['X', 'E', 'E', 'E', 'X'],
    #     ['X', 'X', 'X', 'X', 'E'],
    # ]
    # print(hugo_solution(matrix, word))

    # word = 'ZEEEE'
    # matrix = [
    #     ['Z', 'Z', 'E', 'E', 'X', 'Z'],
    #     ['Z', 'E', 'E', 'E', 'X', 'X'],
    #     ['X', 'E', 'Z', 'E', 'X', 'Z'],
    #     ['X', 'X', 'E', 'E', 'E', 'X'],
    #     ['X', 'Z', 'E', 'X', 'E', 'E'],
    #     ['X', 'Z', 'X', 'X', 'X', 'X'],
    # ]
    # print(hugo_solution(matrix, word))

    word = 'ZZZZZ'
    matrix = [
        ['Z', 'X', 'Z', 'X'],
        ['X', 'Z', 'X', 'Z'],
        ['X', 'X', 'X', 'X'],
        ['Z', 'Z', 'X', 'Z'],
        ['Z', 'Z', 'X', 'Z'],
    ]
    print(hugo_solution(matrix, word))


def next_position(position, add_to_position, max_i, max_j):
    i, j = position
    add_to_i, add_to_j = add_to_position
    new_i, new_j = i + add_to_i, j + add_to_j

    maximum_ok = new_i <= max_i and new_j <= max_j
    minimum_ok = new_i >= 0 and new_j >= 0
    return (new_i, new_j) if maximum_ok and minimum_ok else None


top = partial(
    next_position, add_to_position=(-1, 0), max_i=float('inf'), max_j=float('inf'))
top_right = partial(next_position, add_to_position=(-1, +1), max_i=float('inf'))
right = partial(next_position, add_to_position=(0, +1), max_i=float('inf'))
right_bottom = partial(next_position, add_to_position=(+1, +1))
bottom = partial(next_position, add_to_position=(+1, 0), max_j=float('inf'))
bottom_left = partial(next_position, add_to_position=(+1, -1), max_j=float('inf'))
left = partial(
    next_position, add_to_position=(0, -1), max_i=float('inf'), max_j=float('inf'))
left_top = partial(
    next_position, add_to_position=(-1, -1), max_i=float('inf'), max_j=float('inf'))



get_next_positions = [
    top, top_right, right, right_bottom, bottom, bottom_left, left, left_top]


def hugo_solution(matrix, word):
    char_to_positions = {char: set() for char in word}
    for i, line in enumerate(matrix):
        for j, char in enumerate(line):
            if char in char_to_positions:
                char_to_positions[char].add((i, j))
    print('Matrix')
    pp(matrix)
    print(f"Word '{word}'")
    print('char_to_positions')
    pp(char_to_positions)

    start_positions = char_to_positions[word[0]]

    max_i = len(matrix)
    max_j = len(matrix[0])
    print()
    for position in start_positions:
        current_position = position
        for get_next_position in get_next_positions:
            next_position = current_position
            for i, char in enumerate(word[1:], 1):
                print('Analysing char:', char)
                print('current_position', next_position)
                next_position = get_next_position(
                    next_position, max_i=max_i, max_j=max_j)
                print('next_position', next_position)
                if next_position is None:
                    break
                next_positions = char_to_positions[char]
                if next_position not in next_positions:
                    break
                if i == len(word) - 1:
                    return True
            print()

    return False


def test_top():
    assert top((1, 1)) == (0, 1)
    assert top((0, 1)) is None


def test_top_right():
    assert top_right((1, 1), max_j=6) == (0, 2)
    assert top_right((1, 5), max_j=6) == (0, 6)
    assert top_right((1, 6), max_j=6) is None
    assert top_right((0, 6), max_j=6) is None


def test_right():
    assert right((1, 1), max_j=6) == (1, 2)
    assert right((1, 5), max_j=6) == (1, 6)
    assert right((1, 6), max_j=6) is None


def test_right_bottom():
    assert right_bottom((1, 1), max_i=6, max_j=6) == (2, 2)
    assert right_bottom((5, 5), max_i=6, max_j=6) == (6, 6)
    assert right_bottom((5, 5), max_i=5, max_j=5) is None


def test_bottom():
    assert bottom((1, 1), max_i=6) == (2, 1)
    assert bottom((5, 1), max_i=6) == (6, 1)
    assert bottom((5, 1), max_i=5) is None


def test_bottom_left():
    assert bottom_left((1, 1), max_i=6) == (2, 0)
    assert bottom_left((5, 1), max_i=6) == (6, 0)
    assert bottom_left((5, 1), max_i=5) is None
    assert bottom_left((5, 0), max_i=6) is None


def test_left():
    assert left((1, 1)) == (1, 0)
    assert left((1, 0)) is None


def test_left_top():
    assert left_top((1, 1)) == (0, 0)
    assert left_top((0, 1)) is None
    assert left_top((1, 0)) is None


if __name__ == '__main__':
    main()

"""
Last output

Matrix
[['X', 'E', 'E', 'E', 'X'],
 ['X', 'E', 'Z', 'E', 'X'],
 ['X', 'E', 'E', 'E', 'X'],
 ['XX', 'X', 'X', 'E']]
Word 'ZEE'
char_to_positions
{'Z': {(1, 2)},
 'E': {(0, 1), (2, 1), (1, 1), (0, 3), (2, 3), (0, 2), (3, 3), (2, 2), (1, 3)}}

Analysing char: E
current_position (1, 2)
next_position (0, 2)
Analysing char: E
current_position (0, 2)
next_position None

Analysing char: E
current_position (1, 2)
next_position (0, 3)
Analysing char: E
current_position (0, 3)
next_position None

Analysing char: E
current_position (1, 2)
next_position (1, 3)
Analysing char: E
current_position (1, 3)
next_position (1, 4)

Analysing char: E
current_position (1, 2)
next_position (2, 3)
Analysing char: E
current_position (2, 3)
next_position (3, 4)

Analysing char: E
current_position (1, 2)
next_position (2, 2)
Analysing char: E
current_position (2, 2)
next_position (3, 2)

Analysing char: E
current_position (1, 2)
next_position (2, 1)
Analysing char: E
current_position (2, 1)
next_position (3, 0)

Analysing char: E
current_position (1, 2)
next_position (1, 1)
Analysing char: E
current_position (1, 1)
next_position (1, 0)

Analysing char: E
current_position (1, 2)
next_position (0, 1)
Analysing char: E
current_position (0, 1)
next_position None

False

"""