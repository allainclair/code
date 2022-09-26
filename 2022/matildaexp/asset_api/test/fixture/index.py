from pytest import fixture

from logic.index import IndexLogic
from model_db.index import Index

from test.fixture.database import engine


@fixture
def index_dict_1():
    return {
        'name': 'Index 1',
        'value': 0.05,
    }


@fixture
def index_dict_2():
    return {
        'name': 'Index 2',
        'value': 0.05,
    }


@fixture
def index_dicts(index_dict_1, index_dict_2):
    return [
        index_dict_1 | {'id': 1},
        index_dict_2 | {'id': 2},
    ]


@fixture
def index_model_1(index_dict_1):
    return Index(**index_dict_1)


@fixture
def index_model_1_repeated(index_dict_1):
    return Index(**index_dict_1)


@fixture
def index_model_2(index_dict_2):
    return Index(**index_dict_2)


@fixture
def index_models(index_dicts):
    return [Index(**asset_dict) for asset_dict in index_dicts]


@fixture
def index_logic_populated(engine, index_models):
    index_logic = IndexLogic(engine)
    for index in index_models:
        index_logic.create(index)
    return index_logic
