def structure_data(data):
    data = data.split('\n')
    print(data)

    new_data = []
    for element in data:
        product_id, price = element.split(',')
        product_id, price = int(product_id), float(price)
        new_data.append((product_id, price))
    print(new_data)
    return new_data


def highest_revenue_item(data):
    count_dict = {}
    price_dict = {}

    row_data = data.split()
    for row in row_data:
        txn = row.split(',')
        product_id = txn[0]
        price = txn[1]

        if product_id in count_dict:
            count_dict[product_id] += 1
            if price_dict[product_id] != price:
                return -1
        else:
            count_dict[product_id] = 1
            price_dict[product_id] = price

    most_common_item = '0'
    most_revenue = '0'

    for product in count_dict:
        product_revenue = price_dict[product] * count_dict[product]
        if product_revenue > most_revenue:
            most_revenue = product_revenue
            most_common_item = product

    if most_revenue > '0':
        return int(most_common_item)
    return -1


def main():
    in_ = """111, 5
    111, 5
    222, 3
    333, 6
    333, 6"""
    # in_ = (str("123,1, 234,2 345,3 456,4 567,5"))

    print(in_)
    print(highest_revenue_item(in_))


def test_structure_data():
    in_ = """111, 5
    111, 5
    111, 5
    222, 3
    333, 6
    333, 6"""
    assert structure_data(in_) == [(111, 5.0), (111, 5.0), (111, 5.0), (222, 3), (333, 6), (333, 6)]

if __name__ == '__main__':
    main()
