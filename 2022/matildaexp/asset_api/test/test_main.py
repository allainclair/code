from main import app

from fastapi.testclient import TestClient

from url_v1 import ASSETS
from url_v1 import ASSET
from url_v1 import INDEXES
from url_v1 import INDEX
from exception_detail import ASSET_ALREADY_EXISTS
from exception_detail import ASSET_NOT_FOUND
from exception_detail import INDEX_ALREADY_EXISTS
from exception_detail import INDEX_NOT_FOUND

from test.asset_api.logic.test_index import reset_indexes
from test.asset_api.logic.test_asset import reset_assets


client = TestClient(app)



# Indexes
test_indexes = []


def test_create_index_ok(reset_indexes):
    index = {'name': 'Test Index Name', 'value': 0.1}
    to_create_index = index | {'id': 0}
    response = client.post(f'/{INDEXES}', json=index)
    test_indexes.append(to_create_index)

    assert response.status_code == 200
    assert response.json() == to_create_index


def test_create_index_with_wrong_json():
    index = {'name': 'Test Index Name', 'value': 'wrong_value_type'}
    response = client.post(f'/{INDEXES}', json=index)
    assert response.status_code == 422


def test_create_index_duplicated():
    index = {'name': 'New Index Name', 'value': 0.2}
    to_create_index = index | {'id': 1}
    response = client.post(f'/{INDEXES}', json=index)
    assert response.status_code == 200
    assert response.json() == to_create_index
    test_indexes.append(to_create_index)

    response = client.post(f'/{INDEXES}', json=index)
    assert response.status_code == INDEX_ALREADY_EXISTS.status_code
    assert response.json()['detail'] == INDEX_ALREADY_EXISTS.detail


def test_get_indexes():
    response = client.get(f'/{INDEXES}')
    assert response.status_code == 200
    assert response.json() == test_indexes


def test_get_index():
    index = test_indexes[0]
    response = client.get(f"/{INDEX}/{index['id']}")
    assert response.status_code == 200
    assert response.json() == index


def test_get_index_not_int_id():
    response = client.get(f'/{INDEX}/wrong_id')
    assert response.status_code == 422


def test_get_index_non_existing_id():
    response = client.get(f'/{INDEX}/123456')
    assert response.status_code == INDEX_NOT_FOUND.status_code
    assert response.json()['detail'] == INDEX_NOT_FOUND.detail
