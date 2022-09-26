from pprint import pp


def partitions(arr):
    len_ = len(arr)
    for i in range(len_):
        yield (arr[0:i], i, arr[i + 1:])


def balancedSum(arr):
    parts = ((arr[0:i], i, arr[i + 1:]) for i in range(len(arr)))
    for part in parts:
        left, pivot, right = part
        if sum(left) == sum(right):
            return pivot


def generate_elements(arr):
    len_ = len(arr)

    left_sum = 0
    pivot = 0
    right_sum = sum(arr[1:])
    yield left_sum, pivot, right_sum  # First

    for i in range(1, len_ - 1):
        left_sum += arr[i-1]
        right_sum -= arr[i]
        yield left_sum, i, right_sum


def main():
    r = list(range(10))
    print(r)
    gen = generate_elements(r)
    for t in gen:
        pp(t)
    # pp(partitions(r))



    # in_ = [1, 2, 3, 3]
    # out = balancedSum(in_)
    # print(out)
    # assert out == 2
    #
    # in_ = [1, 2, 1]
    # out = balancedSum(in_)
    # print(out)
    # assert out == 1


if __name__ == '__main__':
    main()
