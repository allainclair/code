from statistics import mean

from config import (
    URL_PRODUCTS,
    ConfigEnum)
from product import Product
from service import get_products


def get_all_products(attributes_conf, sorted_=True):
    service_products = get_products(URL_PRODUCTS)
    products = list(_build_products(service_products, attributes_conf))
    unique_products = set(products)
    return sorted(unique_products) if sorted_ else unique_products


def get_average_price(products):
    return mean(product.price for product in products)


def get_unique_brands(products):
    return set(product.brand_name for product in products)


def _build_products(service_products, configuration=ConfigEnum.NO_REMOVAL):
    def _build():
        for service_product in service_products:
            # If there is any attribute ({'deleted', 'hidden'}),
            # we do not yield the product.
            product = Product(**service_product)
            if all(not getattr(product, attr) for attr in filtering_attributes):
                yield product

    _build_options = {
        ConfigEnum.NO_REMOVAL: {},
        ConfigEnum.REMOVE_DELETED: {'deleted'},
        ConfigEnum.REMOVE_HIDDEN: {'hidden'},
        ConfigEnum.REMOVE_DELETED_AND_HIDDEN: {'deleted', 'hidden'},
    }
    filtering_attributes = _build_options[configuration]
    return _build()
