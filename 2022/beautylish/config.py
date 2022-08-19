from enum import IntEnum

URL_PRODUCTS = 'https://www.beautylish.com/rest/interview-product/list'


class ConfigEnum(IntEnum):
    NO_REMOVAL = 0
    REMOVE_DELETED = 1
    REMOVE_HIDDEN = 2
    REMOVE_DELETED_AND_HIDDEN = 3
