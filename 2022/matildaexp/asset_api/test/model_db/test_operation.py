from pytest import raises

from sqlalchemy.orm.exc import UnmappedInstanceError

from model_db.asset import Asset
from model_db.operation import (
    delete_by_id,
    save_and_refresh,
    select_all,
    select_first_by_id,
    update_and_refresh_by_id)

from test.fixture.database import engine
from test.fixture.asset import (
    asset_dict_1,
    asset_dict_2,
    asset_model_1,
    asset_model_2)


def test_delete_by_id_ok(engine, asset_model_1):
    assert save_and_refresh(engine, asset_model_1)
    assert delete_by_id(engine, Asset, asset_model_1.id)


def test_delete_by_id_not_found(engine):
    assert not delete_by_id(engine, Asset, 'to_not_find_id')


def test_save_and_refresh(engine, asset_model_1):
    assert save_and_refresh(engine, asset_model_1)


def test_save_and_refresh_with_wrong_instance_model(engine):
    with raises(UnmappedInstanceError):
        save_and_refresh(engine, 'wrong_instance_model')


def test_save_and_refresh_with_wrong_engine(asset_model_1):
    with raises(AttributeError):
        save_and_refresh('engine', asset_model_1)


def test_select_all(engine, asset_model_1, asset_model_2):
    assert save_and_refresh(engine, asset_model_1)
    assert save_and_refresh(engine, asset_model_2)
    assets = select_all(engine, Asset)
    assert len(assets) == 2
    assert asset_model_1 in assets and asset_model_2 in assets


def test_select_first_by_id(engine, asset_model_1):
    assert save_and_refresh(engine, asset_model_1)
    assert select_first_by_id(engine, Asset, asset_model_1.id) == asset_model_1


def test_select_first_by_id_with_wrong_id(engine):
    assert select_first_by_id(engine, Asset, 'wrong_id') is None


def test_update_and_refresh_by_id_ok(engine, asset_model_1, asset_model_2):
    assert save_and_refresh(engine, asset_model_1)
    current_id = asset_model_1.id
    assert update_and_refresh_by_id(
        engine, Asset, current_id, asset_model_2) == asset_model_2


def test_update_and_refresh_by_id_not_found(engine, asset_model_1):
    assert not update_and_refresh_by_id(engine, Asset, asset_model_1.id, asset_model_1)
