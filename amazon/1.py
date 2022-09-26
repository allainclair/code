def getMinMoves(plates):
    len_ = len(plates)
    max_index = plates.index(max(plates))
    min_index = plates.index(min(plates))

    max_moves = len_ - max_index - 1
    min_moves = min_index

    moves = max_moves + min_moves
    if max_index < min_index:
        moves -= 1

    return moves



def main():
    plates = [3, 2, 1]
    assert getMinMoves(plates) == 3
    plates = [2, 4, 3, 1, 6]
    assert getMinMoves(plates) == 3
    plates = [4, 11, 9, 10, 12]
    assert getMinMoves(plates) == 0


if __name__ == '__main__':
    main()
