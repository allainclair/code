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


"""

from pprint import pp


def main():
    matrix = [
        ['A', 'U', 'I', 'K', 'F', 'W', 'N'],
        ['W', 'Q', 'B', 'O', 'L', 'X', 'P'],
        ['T', 'L', 'A', 'E', 'R', 'E', 'S'],
        ['Y', 'Z', 'X', 'E', 'R', 'L', 'W'],
    ]
    word = 'UBER'
    print(hugo_solution(matrix, word))


def top(position):
    i, j = position
    return i - 1, j


def top_right(position):
    i, j = position
    return i - 1, j + 1


def right(position):
    i, j = position
    return i, j + 1


def right_bottom(position):
    i, j = position
    return i + 1, j + 1


def bottom(position):
    i, j = position
    return i + 1, j


def bottom_left(position):
    i, j = position
    return i + 1, j - 1


def left(position):
    i, j = position
    return i, j - 1


def left_top(position):
    i, j = position
    return i - 1, j - 1


def hugo_solution(matrix, word):
    char_to_positions = {char: set() for char in word}
    for i, line in enumerate(matrix):
        for j, char in enumerate(line):
            if char in char_to_positions:
                char_to_positions[char].add((i, j))

    pp(char_to_positions)

    start_positions = char_to_positions[word[0]]

    # for position in start_positions:
    #     for char in word[1:]:
    #         x(matrix, position, char)


def test_top():
    assert top((1, 1)) == (0, 1)


def test_top_right():
    assert top_right((1, 1)) == (0, 2)


def test_right():
    assert right((1, 1)) == (1, 2)


def test_right_bottom():
    assert right_bottom((1, 1)) == (2, 2)


def test_bottom():
    assert bottom((1, 1)) == (2, 1)


def test_bottom_left():
    assert bottom_left((1, 1)) == (2, 0)


def test_left():
    assert left((1, 1)) == (1, 0)


def test_left_top():
    assert left_top((1, 1)) == (0, 0)


# A  U  I  K
# U  I  K  F
# I  K  F  W

# B  O  L

# UBER in line

# 1. Iterar por toda matriz ateh encontrar uma letra
# 2. Caso encontre: analisar as 8 adjacencias pela segunda letra.
# 3. Caso encontre a segunda letra: analisar o restante na mesma direcao da segunda letra
# 4. Caso passo 3 se concretize, retornamos true
# 5.




#
#
#
# A  A  A  A  F  W  N
# W  Q  B  O  L  X  P
# T  L  A  E  R  E  S
# Y  Z  X  E  R  L  W
#
#

def get_position(A):
    for i, _ in enumerate(A):
        for j, _ in enumerate(A[i]):
            yield i, j


def get_adjacency_words(A, coord, word_len):
    start_i, start_j = coord

    try:
        word = ''

        for k in range(word_len):
            word += A[start_i][start_j + k]
        yield word
    except KeyError:
        pass

    try:
        word = ''
        for k in range(word_len):
            word += A[start_i + k][start_j]
        yield word
    except KeyError:
        pass

    try:
        word = ''
        for k in range(word_len):
            word += A[start_i][start_j - k]
        yield word
    except KeyError:
        pass

    try:
        word = ''
        for k in range(word_len):
            word += A[start_i - k][start_j]
        yield word
    except KeyError:
        pass


def parse_adjacencies(A, coord, word):
    len_ = len(word)
    for parsing_word in get_adjacency_words(A, coord, len_):
        if parsing_word == word:
            return True
    return False


def solution(A, word):
    generator = get_position(A)
    for coord in generator:
        if parse_adjacencies(A, coord, word):
            return True
    return False


# Test get_position
# gen = get_position(A)

# for char in gen:
#     print(char)

#
# print(solution(A, 'UBER'))
# print('Hello')
if __name__ == '__main__':
    main()
