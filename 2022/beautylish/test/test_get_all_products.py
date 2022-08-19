"""End-to-end test that tests the 3 requirements:
1. Sorted by prices and if the prices are equal, sort by name
2. No hidden and no deleted product in the list.
3. Unique products only.
"""
from config import ConfigEnum
from logic import get_all_products


products = get_all_products(ConfigEnum.REMOVE_DELETED_AND_HIDDEN)


def test_price_and_name():
    for product_1, product_2 in zip(products[:-1], products[1:]):
        if product_1.price == product_2.price:
            assert product_1.product_name <= product_2.product_name
        else:
            assert product_1.price < product_2.price


def test_no_hidden_and_no_deleted_product():
    assert not any(p for p in products if p.hidden or p.deleted)


def test_only_unique_products():
    # Product list and set must have the same length.
    assert len(set(products)) == len(products)
