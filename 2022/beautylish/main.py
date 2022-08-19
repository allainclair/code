from config import ConfigEnum
from logic import (
    get_all_products,
    get_average_price,
    get_unique_brands,
)
from view import display


def main():
    products = get_all_products(ConfigEnum.REMOVE_DELETED_AND_HIDDEN)

    # Average and unique brands
    # from the unique products excluding hidden and/or deleted.
    average_price = get_average_price(products)
    unique_brands = get_unique_brands(products)

    display(average_price, products, unique_brands)


if __name__ == '__main__':
    main()
