from pytest import fixture

from product import Product


@fixture
def product_1(product_1_dict):
    return Product(**product_1_dict)


@fixture
def product_1_equal(product_1_dict):
    return Product(**product_1_dict)


@fixture
def product_2(product_2_dict):
    return Product(**product_2_dict)


@fixture
def product_deleted(product_deleted_dict):
    return Product(**product_deleted_dict)


@fixture
def product_hidden(product_hidden_dict):
    return Product(**product_hidden_dict)


@fixture
def product_deleted_and_hidden(product_deleted_and_hidden_dict):
    return Product(**product_deleted_and_hidden_dict)
