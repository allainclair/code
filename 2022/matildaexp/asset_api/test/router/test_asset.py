from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import fixture

from logic.asset import AssetLogic
from router import asset
from router.exception_detail import (
    ASSET_ALREADY_EXISTS,
    ASSET_NOT_FOUND)
from router.url_v1 import URL_ASSET

from test.fixture.database import engine
from test.fixture.asset import (
    asset_dict_1,
    asset_dict_2,
    asset_dicts,
    asset_logic_populated,
    asset_models)

app = FastAPI()
app.include_router(asset.router)
client = TestClient(app)


@fixture
def fixture_asset_logic(engine):
    return AssetLogic(engine)


def test_create_asset_ok(fixture_asset_logic, asset_dict_1):
    asset.asset_logic = fixture_asset_logic
    to_create_asset = asset_dict_1 | {'id': 1}

    response = client.post(f'{URL_ASSET}', json=asset_dict_1)
    assert response.status_code == 200
    assert response.json() == to_create_asset


def test_create_asset_with_wrong_types(asset_dict_1):
    asset_dict_1['fix_interest'] = 'wrong_fix_interest'
    asset_dict_1['duration'] = 'wrong_duration_type'
    response = client.post(f'{URL_ASSET}', json=asset_dict_1)
    assert response.status_code == 422


def test_create_asset_duplicated(fixture_asset_logic, asset_dict_1):
    asset.asset_logic = fixture_asset_logic

    assert client.post(f'{URL_ASSET}', json=asset_dict_1)
    response = client.post(f'{URL_ASSET}', json=asset_dict_1)
    assert response.status_code == ASSET_ALREADY_EXISTS.status_code
    assert response.json()['detail'] == ASSET_ALREADY_EXISTS.detail


def test_get_assets(asset_logic_populated, asset_dicts):
    asset.asset_logic = asset_logic_populated

    response = client.get(f'{URL_ASSET}')
    assert response.status_code == 200
    assert response.json() == asset_dicts


def test_get_asset(asset_logic_populated, asset_dict_1):
    asset.asset_logic = asset_logic_populated

    asset_dict_1['id'] = 1
    response = client.get(f"{URL_ASSET}/{asset_dict_1['id']}")
    assert response.status_code == 200
    assert response.json() == asset_dict_1


def test_get_asset_is_not_int_id():
    response = client.get(f'{URL_ASSET}/wrong_id')
    assert response.status_code == 422


def test_get_asset_non_existing_id(fixture_asset_logic):
    asset.asset_logic = fixture_asset_logic

    response = client.get(f'{URL_ASSET}/123456')
    assert response.status_code == ASSET_NOT_FOUND.status_code
    assert response.json()['detail'] == ASSET_NOT_FOUND.detail
