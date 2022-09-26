def main():
    pass


def mergesort(list_, start, len_):
    mid = _get_mid(start, len_)
    if len_ <= start:
        return []


    _merge()



def _merge(list_):
    pass


def _get_mid(start, len_):
    segment_len = len_ - start
    mid = segment_len // 2
    return mid + start


def test__get_mid():
    start, len_ = 0, 16
    assert _get_mid(start, len_) == 8

    start, len_ = 0, 32
    assert _get_mid(start, len_) == 16

    start, len_ = 16, 32
    assert _get_mid(start, len_) == 24


if __name__ == '__main__':
    main()
