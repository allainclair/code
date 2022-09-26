from pytest import fixture
from logic.asset import AssetLogic

from test.fixture.asset import (
    asset_dict_1,
    asset_dict_2,
    asset_model_1,
    asset_model_1_repeated,
    asset_model_2)
from test.fixture.database import engine


@fixture
def asset_logic(engine):
    return AssetLogic(engine)


class TestAssetLogic:
    def test_create(self, asset_logic, asset_model_1, asset_model_2):
        assert asset_logic.create(asset_model_1)
        assert asset_logic.create(asset_model_2)

    def test_create_but_fails_due_to_repeated_asset(
            self, asset_logic, asset_model_1, asset_model_1_repeated):
        assert asset_logic.create(asset_model_1)
        assert not asset_logic.create(asset_model_1_repeated)
        assert not asset_model_1_repeated.saved

    def test_get_ok(self, asset_logic, asset_model_1):
        assert asset_logic.create(asset_model_1)
        assert asset_logic.get(asset_id=1) == asset_model_1

    def test_get_not_found(self, asset_logic):
        assert asset_logic.get(10) is None

    def test_get_all(self, asset_logic, asset_model_1, asset_model_2):
        assert asset_logic.create(asset_model_1)
        assert asset_logic.create(asset_model_2)

        instances = asset_logic.get_all()
        assert len(instances) == 2
        assert asset_model_1 in instances and asset_model_2 in instances
