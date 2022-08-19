from json import loads
from urllib import request
from urllib.error import URLError

from config import URL_PRODUCTS

from logging import getLogger

logger = getLogger(__name__)


def get_products(url=URL_PRODUCTS):
    try:
        resource = request.urlopen(url)
        resource_body = resource.read()
        json_object = loads(resource_body.decode('utf-8'))
        return json_object['products']
    except URLError:
        logger.warning(f"Could not get products from '{url}'")
        raise Warning(f"Could not get products from '{url}'")
