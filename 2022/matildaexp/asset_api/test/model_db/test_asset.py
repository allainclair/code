from pytest import raises
from sqlalchemy.exc import IntegrityError

from model_db.asset import Asset
from model_db.operation import (
    save_and_refresh,
    select_first_by_id)

from test.fixture.database import engine
from test.fixture.asset import (
    asset_dict_1,
    asset_dict_2,
    asset_model_1,
    asset_model_1_repeated,
    asset_model_2)


def test_add_asset_without_id(engine, asset_model_1):
    assert asset_model_1.id is None
    assert save_and_refresh(engine, asset_model_1)
    assert asset_model_1.saved
    assert select_first_by_id(engine, Asset, asset_model_1.id) == asset_model_1


def test_add_asset_with_id(engine, asset_model_2):
    id_ = 9999
    asset_model_2.id = id_
    assert save_and_refresh(engine, asset_model_2)
    assert asset_model_2.saved
    assert select_first_by_id(engine, Asset, asset_model_2.id) == asset_model_2
    assert asset_model_2.id == id_


def test_add_asset_but_fails_due_to_repeated_asset_name(
        engine, asset_model_1, asset_model_1_repeated):
    assert save_and_refresh(engine, asset_model_1)
    with raises(IntegrityError):
        assert save_and_refresh(engine, asset_model_1_repeated)
