LJUST = 16


def display_unique_products(products):
    print('List of unique products:\n')
    for product in products:
        print(
            f"{'Brand name:'.ljust(LJUST)}{product.brand_name}\n"
            f"{'Product name:'.ljust(LJUST)}{product.product_name}\n"
            f"{'Product price:'.ljust(LJUST)}${product.price:.2f}\n"
        )


def display(average_price, unique_products, unique_brands):
    display_unique_products(unique_products)
    print('Summary:')
    print(f'Total number of unique products: {len(unique_products)}')
    print(f'Total number of unique brands: {len(unique_brands)}')
    print(f'Average price: {average_price:.2f}')
