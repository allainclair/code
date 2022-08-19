"""Exercise to calculate the minimal_number_of_packages given
items, the number of large packages with a capacity of 5,
and small packages of capacity 1.
"""


def not_enough_packages(items, available_large_packages, large_packages_capacity, available_small_packages):
    return items > available_large_packages*large_packages_capacity + available_small_packages


def minimal_number_of_packages(items, available_large_packages, available_small_packages):
    large_packages_capacity = 5

    if not_enough_packages(items, available_large_packages, large_packages_capacity, available_small_packages):
        return -1

    n_large = items // large_packages_capacity
    n_small = items % large_packages_capacity

    rest_large_packages = available_large_packages - n_large
    if rest_large_packages < 0:
        large_packages = available_large_packages
        small_packages = items - (available_large_packages*large_packages_capacity)
    else:
        large_packages = n_large
        small_packages = n_small

    return large_packages + small_packages


def main():
    items = 16
    large = 2
    small = 10
    assert minimal_number_of_packages(items, large, small) == 8


if __name__ == '__main__':
    main()
