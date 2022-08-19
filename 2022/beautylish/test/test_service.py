from json import dumps
from urllib.error import URLError

from unittest.mock import (
    Mock,
    patch,
)

from pytest import raises

from config import URL_PRODUCTS
from service import get_products

from test.fixture_product_dict import (
    product_1,
    product_2,
)


@patch('service.request.urlopen')
def test_get_products(mock_urlopen, product_1, product_2):
    products = {'products': [product_1, product_1, product_2]}
    expected_products = [product_1, product_1, product_2]

    resource = Mock()
    resource.read.return_value = dumps(products, ensure_ascii=False).encode('utf8')
    mock_urlopen.return_value = resource

    got_products = list(get_products(URL_PRODUCTS))
    assert expected_products == got_products


@patch('service.request.urlopen')
def test_get_products_with_exception(mock_urlopen):
    mock_urlopen.side_effect = URLError('Any url error')
    with raises(Warning):
        get_products(URL_PRODUCTS)
