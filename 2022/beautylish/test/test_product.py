from pytest import fixture

from product import (
    Product,
    _parse_price,
    _tail)

from test.fixture_product_dict import (
    product_1,
    product_2,
)


FLOAT_PRICE = 11.11


@fixture
def product_float_price(product_1):
    product_1['price'] = FLOAT_PRICE
    return Product(**product_1)


@fixture
def product_string_price(product_1):
    product_1['price'] = str(FLOAT_PRICE)
    return Product(**product_1)


@fixture
def product_string_with_sign_price(product_1):
    product_1['price'] = f'${FLOAT_PRICE}'
    return Product(**product_1)


def test_product_float_price(product_float_price):
    assert product_float_price.price == FLOAT_PRICE
    assert product_float_price == eval(repr(product_float_price))


def test_product_string_price(product_string_price):
    assert product_string_price.price == FLOAT_PRICE
    assert product_string_price == eval(repr(product_string_price))


def test_product_string_with_sign_price(product_string_with_sign_price):
    assert product_string_with_sign_price.price == FLOAT_PRICE
    assert product_string_with_sign_price == eval(repr(product_string_with_sign_price))


def test_product_equal(product_1):
    p1 = Product(**product_1)
    p2 = Product(**product_1)
    assert p1 == p2


def test_product_different(product_1):
    p1 = Product(**product_1)
    product_1['brand_name'] += ' anything'
    p2 = Product(**product_1)
    assert p1 != p2


def test_product_comparing_p1_cheaper_and_same_names(product_1):
    p1 = Product(**product_1)
    p2 = Product(**product_1)
    p2.price += 1
    assert p1 < p2
    assert not p2 < p1


def test_product_comparing_p1_cheaper_and_p2_post_fix_renaming(product_1):
    p1 = Product(**product_1)
    p2 = Product(**product_1)
    p2.price += 1
    p2.product_name += ' anything'
    assert p1 < p2
    assert not p2 < p1


def test_product_comparing_p1_cheaper_and_p2_pre_fix_renaming(product_1):
    p1 = Product(**product_1)
    p2 = Product(**product_1)
    p2.price += 1
    p2.product_name = f'A prefix to sort it before {p1.product_name}'
    assert p1 < p2
    assert not p2 < p1


def test_product_comparing_same_prices_and_different_names(product_1):
    p1 = Product(**product_1)
    p2 = Product(**product_1)
    p2.product_name += ' anything'
    assert p1 < p2
    assert not p2 < p1


def test__parse_price_float():
    assert _parse_price(11.11) == 11.11


def test__parse_price_string():
    assert _parse_price('11.11') == 11.11


def test__parse_price_string_with_sign():
    assert _parse_price('$11.11') == 11.11


def test__tail():
    assert _tail('$11.11') == '11.11'
