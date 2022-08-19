from pytest import fixture


@fixture
def product_1():
    return {
        'brand_name': 'Brand name 1',
        'deleted': False,
        'hidden': False,
        'id': 1,
        'price': '$11.11',
        'product_name': 'Product 1',
    }


@fixture
def product_2():
    return {
        'brand_name': 'Brand name 2',
        'deleted': False,
        'hidden': False,
        'id': 2,
        'price': '$22.22',
        'product_name': 'Product 2',
    }


@fixture
def product_deleted():
    return {
        'brand_name': 'Brand name',
        'deleted': True,
        'hidden': False,
        'id': 3,
        'price': '$33.33',
        'product_name': 'Product deleted',
    }


@fixture
def product_hidden():
    return {
        'brand_name': 'Brand name',
        'deleted': False,
        'hidden': True,
        'id': 4,
        'price': '$44.44',
        'product_name': 'Product hidden',
    }


@fixture
def product_deleted_and_hidden():
    return {
        'brand_name': 'Brand name',
        'deleted': True,
        'hidden': True,
        'id': 5,
        'price': '$55.55',
        'product_name': 'Product deleted and hidden',
    }
