from unittest.mock import patch

from config import ConfigEnum
from logic import (
    get_all_products,
    get_average_price,
    get_unique_brands,
    _build_products)

from test.fixture_product import (
    product_1,
    product_1_equal,
    product_2,
    product_deleted,
    product_hidden,
    product_deleted_and_hidden,
)
from test.fixture_product_dict import (
    product_1 as prod_1_dict,
    product_2 as prod_2_dict,
    product_deleted as prod_deleted_dict,
    product_hidden as prod_hidden_dict,
    product_deleted_and_hidden as prod_deleted_and_hidden_dict,
)


@patch('logic.get_products')
def test_get_all_products(
        get_products_mock,
        product_1,
        product_2,
        prod_1_dict,
        prod_2_dict):
    excepted_products = [product_1, product_2]
    get_products_mock.return_value = [prod_1_dict, prod_1_dict, prod_2_dict]

    got_products = list(get_all_products(ConfigEnum.NO_REMOVAL))
    assert got_products == excepted_products


@patch('logic.get_products')
def test_get_all_products_empty(get_products_mock):
    excepted_products = []
    get_products_mock.return_value = []

    assert list(get_all_products(ConfigEnum.NO_REMOVAL)) == excepted_products


@patch('logic.get_products')
def test_get_all_products_removing_deleted(
        get_products_mock, product_1, prod_1_dict, prod_deleted_dict):
    get_products_mock.return_value = [prod_1_dict, prod_deleted_dict]
    products_not_deleted = [product_1]

    got_products = get_all_products(ConfigEnum.REMOVE_DELETED)
    assert got_products == products_not_deleted


@patch('logic.get_products')
def test_get_all_products_removing_hidden(
        get_products_mock, product_1, product_1_dict, prod_hidden_dict):
    get_products_mock.return_value = [product_1_dict, prod_hidden_dict]
    products_not_hidden = [product_1]

    got_products = get_all_products(ConfigEnum.REMOVE_HIDDEN)
    assert got_products == products_not_hidden


@patch('logic.get_products')
def test_get_all_products_removing_deleted_and_hidden(
        get_products_mock,
        product_1,
        prod_1_dict,
        prod_deleted_dict,
        prod_hidden_dict,
        prod_deleted_and_hidden_dict):
    get_products_mock.return_value = [
        prod_1_dict,
        prod_deleted_dict,
        prod_hidden_dict,
        prod_deleted_and_hidden_dict,
    ]
    products_not_hidden_and_not_deleted = [product_1]

    got_products = get_all_products(ConfigEnum.REMOVE_DELETED_AND_HIDDEN)
    assert got_products == products_not_hidden_and_not_deleted


@patch('logic.get_products')
def test_get_all_products_sorted_by_price(
        get_products_mock,
        product_1,
        product_1_equal,
        product_2,
        prod_1_dict,
        prod_2_dict):
    assert product_1 == product_1_equal
    product_1_equal.price += 1
    assert product_1 < product_1_equal

    new_price = float(prod_1_dict['price'][1:]) + 1
    new_price_dict = {'price': f'${new_price:.2f}'}
    prod_1_different = prod_1_dict | new_price_dict
    get_products_mock.return_value = [prod_2_dict, prod_1_dict, prod_1_different]
    expected_products = [product_1, product_1_equal, product_2]

    got_products = get_all_products(ConfigEnum.NO_REMOVAL)
    assert got_products == expected_products


@patch('logic.get_products')
def test_get_all_products_sorted_by_name(
        get_products_mock,
        product_1,
        product_1_equal,
        product_2,
        prod_1_dict,
        prod_2_dict):
    assert product_1 == product_1_equal
    product_1_equal.product_name += ' anything'
    assert product_1 < product_1_equal

    prod_1_different = prod_1_dict | {
        'product_name': prod_1_dict['product_name'] + ' anything'
    }
    get_products_mock.return_value = [prod_2_dict, prod_1_dict, prod_1_different]
    expected_products = [product_1, product_1_equal, product_2]

    got_products = get_all_products(ConfigEnum.NO_REMOVAL)
    assert got_products == expected_products


def test_get_average_price(product_1, product_2):
    expected_average = (product_1.price + product_2.price) / 2
    assert get_average_price({product_1, product_2}) == expected_average


def test_get_unique_brands(product_1):
    expected_brands = {product_1.brand_name}
    assert get_unique_brands([product_1, product_1]) == expected_brands


def test__build_products(product_1, product_2, prod_1_dict, prod_2_dict):
    service_products = [prod_1_dict, prod_1_dict, prod_2_dict]
    excepted_products = [product_1, product_1, product_2]  # Allow repeated.
    built_products = list(_build_products(service_products))
    assert built_products == excepted_products


def test__build_products_removing_deleted(product_1, prod_1_dict, prod_deleted_dict):
    service_products = [prod_1_dict, prod_deleted_dict]
    products_not_deleted = [product_1]
    built_products = list(_build_products(service_products, ConfigEnum.REMOVE_DELETED))
    assert built_products == products_not_deleted


def test__build_products_removing_hidden(product_1, prod_1_dict, prod_hidden_dict):
    service_products = [prod_1_dict, prod_hidden_dict]
    products_not_hidden = [product_1]
    built_products = list(_build_products(service_products, ConfigEnum.REMOVE_HIDDEN))
    assert built_products == products_not_hidden


def test__build_products_removing_deleted_and_hidden(
        product_1,
        prod_1_dict,
        prod_deleted_dict,
        prod_hidden_dict):
    service_products = [prod_1_dict, prod_deleted_dict, prod_hidden_dict]
    products_not_deleted_and_not_hidden = [product_1]
    built_products = list(
        _build_products(service_products, ConfigEnum.REMOVE_DELETED_AND_HIDDEN))
    assert built_products == products_not_deleted_and_not_hidden
