from dataclasses import dataclass


@dataclass()
class Product:
    brand_name: str
    deleted: bool
    hidden: bool
    id: int
    price: float | str
    product_name: str

    def __post_init__(self):
        self.price = _parse_price(self.price)

    def __hash__(self):
        return hash(self.__repr__())

    def __lt__(self, other):
        # This function is called when we use sorted
        # Ref: https://docs.python.org/3/library/functions.html#sorted
        if self.price < other.price:
            return True
        elif self.price == other.price and self.product_name < other.product_name:
            return True
        else:
            return False


def _parse_price(price):
    try:
        return float(price)
    except ValueError:
        # Removing first char '$' from start
        return float(_tail(price))


def _tail(price):
    return price[1:]
