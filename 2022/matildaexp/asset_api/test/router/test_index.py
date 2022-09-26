from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import fixture


from logic.index import IndexLogic
from router import index
from router.exception_detail import (
    INDEX_ALREADY_EXISTS,
    INDEX_NOT_FOUND)
from router.url_v1 import URL_INDEX

from test.fixture.database import engine
from test.fixture.index import (
    index_dict_1,
    index_dict_2,
    index_dicts,
    index_logic_populated,
    index_models)

app = FastAPI()
app.include_router(index.router)
client = TestClient(app)

from icecream import ic


@fixture
def fixture_index_logic(engine):
    return IndexLogic(engine)


def test_create_index_ok(fixture_index_logic, index_dict_1):
    index.index_logic = fixture_index_logic
    to_create_index = index_dict_1 | {'id': 1}

    response = client.post(f'{URL_INDEX}', json=index_dict_1)
    assert response.status_code == 200
    assert response.json() == to_create_index


def test_create_index_with_wrong_types(index_dict_1):
    index_dict_1['value'] = 'wrong_value_type'
    response = client.post(f'{URL_INDEX}', json=index_dict_1)
    assert response.status_code == 422


def test_create_index_duplicated(fixture_index_logic, index_dict_1):
    index.index_logic = fixture_index_logic

    assert client.post(f'{URL_INDEX}', json=index_dict_1)
    response = client.post(f'{URL_INDEX}', json=index_dict_1)
    assert response.status_code == INDEX_ALREADY_EXISTS.status_code
    assert response.json()['detail'] == INDEX_ALREADY_EXISTS.detail


def test_get_indexes(index_logic_populated, index_dicts):
    index.index_logic = index_logic_populated

    response = client.get(f'{URL_INDEX}')
    assert response.status_code == 200
    assert response.json() == index_dicts


def test_get_index_ok(index_logic_populated, index_dict_1):
    index.index_logic = index_logic_populated

    index_dict_1['id'] = 1
    response = client.get(f"{URL_INDEX}/{index_dict_1['id']}")
    assert response.status_code == 200
    assert response.json() == index_dict_1


def test_get_index_is_not_int_id():
    response = client.get(f'{URL_INDEX}/wrong_id')
    assert response.status_code == 422


def test_get_index_non_existing_id(fixture_index_logic):
    index.index_logic = fixture_index_logic

    response = client.get(f'{URL_INDEX}/123456')
    assert response.status_code == INDEX_NOT_FOUND.status_code
    assert response.json()['detail'] == INDEX_NOT_FOUND.detail


def test_delete_index_ok(index_logic_populated, index_dict_1):
    index.index_logic = index_logic_populated

    index_dict_1['id'] = 1
    response = client.delete(f"{URL_INDEX}/{index_dict_1['id']}")
    assert response.status_code == 200
    assert response.json() == index_dict_1


def test_delete_index_non_existing_id(fixture_index_logic):
    index.index_logic = fixture_index_logic

    response = client.delete(f'{URL_INDEX}/123456')
    assert response.status_code == INDEX_NOT_FOUND.status_code
    assert response.json()['detail'] == INDEX_NOT_FOUND.detail


def test_update_index_ok(index_logic_populated, index_dict_1):
    index.index_logic = index_logic_populated

    response = client.put(f"{URL_INDEX}/1", json=index_dict_1)
    index_dict_1['id'] = 1
    assert response.status_code == 200
    assert response.json() == index_dict_1


def test_update_index_non_existing_id(fixture_index_logic, index_dict_1):
    index.index_logic = fixture_index_logic

    response = client.put(f'{URL_INDEX}/123456', json=index_dict_1)
    assert response.status_code == INDEX_NOT_FOUND.status_code
    assert response.json()['detail'] == INDEX_NOT_FOUND.detail
