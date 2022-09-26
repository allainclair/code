import json

from marshmallow import Schema, fields

from pprint import pp

DATA_PATH = 'data/categories.json'
PRODUCTS_DATA_PATH = 'data/products.json'


class Category:
    def __int__(self):
        pass

    @classmethod
    def get_all(cls):
        category_schema = CategorySchema(many=True)
        with open(DATA_PATH) as f:
            category_objects = json.load(f)
            category_objects = get_counting_products(category_objects)
            return category_schema.dump(category_objects)


# [{"id":1,"name":"Games","is_active":false,"created_at":"2022-06-15","birth_date":"1998-01-25"},
class CategorySchema(Schema):
    id = fields.Int()
    name = fields.Str()
    is_active = fields.Bool()
    created_at = fields.Str()
    birth_date = fields.Str()
    count = fields.Int()


def get_counting_products(category_objects):
    category_by_id = {}
    for category in category_objects:
        category['count'] = 0
        category_by_id[category['id']] = category

    # pp(category_by_id)

    with open(PRODUCTS_DATA_PATH) as f:
        products_objects = json.load(f)
        for product in products_objects:
            prod_category_id = product['category_id']
            category = category_by_id[prod_category_id]
            pp(category)
            category['count'] += 1
    return list(category_by_id.values())
