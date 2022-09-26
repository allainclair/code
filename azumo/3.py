from requests import get

from pprint import pprint

URL = 'https://jsonmock.hackerrank.com/api/food_outlets?city={}&page={}'


def filter_outlets(outlets, max_cost):
    return [
        outlet['name']
        for outlet in outlets
        if outlet['estimated_cost'] <= max_cost]


def getRelevantFoodOutlets(city, maxCost):
    first_resources = get(URL.format(city, 1)).json()

    cities = first_resources['data']
    filtered_outlet_names = filter_outlets(cities, maxCost)
    total_pages = first_resources['total_pages']

    for page_number in range(2, total_pages + 1):  # One page already requested.
        resources = get(URL.format(city, page_number))
        filtered_outlet_names += filter_outlets(resources.json()['data'], maxCost)

    return filtered_outlet_names


def main():
    city = ''
    maxCost = 0
    resources = getRelevantFoodOutlets(city, maxCost)
    # pp(resources)


if __name__ == '__main__':
    main()
