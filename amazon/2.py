from pprint import pp


def sublists(list_):
    for i, _ in enumerate(list_):
        sublist = list_[i:]
        for j, _ in enumerate(sublist):
            yield sublist[:len(sublist)-j]


def sublists_2(list_):
    for i, _ in enumerate(list_):
        sublist = list_[i:]
        for j, _ in enumerate(sublist):
            yield sublist[len(sublist)-j-1:]


def try_cache(prods, cache):
    number_of_products = None
    cached_prod_number = cache.get(tuple(prods[1:]))  #
    if cached_prod_number is not None:
        if prods[0] < cached_prod_number:
            number_of_products = prods[0] + cached_prod_number
        else:
            number_of_products = cached_prod_number - 1
    return number_of_products


def findMaxProducts(products):
    sub_products = sublists(products)
    max_products = 0
    cache = {}
    for prods in sub_products:
        number_of_products = try_cache(prods, cache)
        if number_of_products is None:
            reversed_prods = prods[::-1]

            previous_number_of_products = float('Inf')
            number_of_products = 0
            for n_products in reversed_prods:
                if n_products < previous_number_of_products:
                    number_of_products += n_products
                    previous_number_of_products = n_products
                else:
                    previous_number_of_products -= 1
                    number_of_products += previous_number_of_products
            cache[tuple(prods)] = number_of_products

        if number_of_products > max_products:
            max_products = number_of_products

    return max_products


# def sublists(list_):
#     for i, _ in enumerate(list_):
#         sublist = list_[i:]
#         for j, _ in enumerate(sublist):
#             yield sublist[:len(sublist) - j]
#
#
# def findMaxProducts(products):
#     sub_products = sublists(products)
#     max_products = 0
#     for prods in sub_products:
#         reversed_prods = prods[::-1]
#
#         previous_number_of_products = float('Inf')
#         number_of_products = 0
#         for n_products in reversed_prods:
#             if n_products < previous_number_of_products:
#                 number_of_products += n_products
#                 previous_number_of_products = n_products
#             else:
#                 previous_number_of_products -= 1
#                 number_of_products += previous_number_of_products
#
#         if number_of_products > max_products:
#             max_products = number_of_products
#
#     return max_products



def main():
    products = [2, 5, 6, 7]
    pp(list(sublists_2(products)))
    assert findMaxProducts(products) == 20

    products = [2, 9, 4, 7, 5, 2]
    assert findMaxProducts(products) == 16


if __name__ == '__main__':
    main()
