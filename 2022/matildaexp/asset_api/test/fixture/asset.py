from pytest import fixture

from logic.asset import AssetLogic
from model_db.asset import Asset

from test.fixture.database import engine


@fixture
def asset_dict_1():
    return {
        'name': 'Asset 1',
        'ir': 0.2,
        'fix_interest': 0.05,
        'duration': 1,
        'id_index': 1,
    }


@fixture
def asset_dict_2():
    return {
        'name': 'Asset 2',
        'ir': 0.2,
        'fix_interest': 0.05,
        'duration': 1,
        'id_index': 1,
    }


@fixture
def asset_dicts(asset_dict_1, asset_dict_2):
    return [
        asset_dict_1 | {'id': 1},
        asset_dict_2 | {'id': 2},
    ]


@fixture
def asset_model_1(asset_dict_1):
    return Asset(**asset_dict_1)


@fixture
def asset_model_1_repeated(asset_dict_1):
    return Asset(**asset_dict_1)


@fixture
def asset_model_2(asset_dict_2):
    return Asset(**asset_dict_2)


@fixture
def asset_models(asset_dicts):
    return [Asset(**asset_dict) for asset_dict in asset_dicts]


@fixture
def asset_logic_populated(engine, asset_models):
    asset_logic = AssetLogic(engine)
    for asset in asset_models:
        asset_logic.create(asset)
    return asset_logic
