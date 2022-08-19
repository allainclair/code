import pytest

# caching_data = {}


def caching(func):
    caching_data = {}

    def wrapper(n):
        if n not in caching_data:
            output = func(n)
            caching_data[n] = output
            return output
        else:
            return caching_data[n]
    return wrapper


@caching
def fib(n):
    if n < 0:
        return ValueError('Negative numbers not allowed')
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_2():
    yield 0
    yield 1
    i = 2
    while True:
        yield fib(i)
        i += 1


def test_negative():
    with pytest.raises(ValueError):
        fib(-2)


def test_0():
    assert fib(0) == 0


def test_1():
    assert fib(1) == 1


def test_2():
    assert fib(2) == 1


def test_3():
    assert fib(3) == 2


def test_4():
    assert fib(4) == 3


def test_10():
    output = fib(50)
    assert output == 12586269025


def test_generator():
    gen = fib_2()
    for x in range(10+1):
        assert fib(x) == next(gen)
