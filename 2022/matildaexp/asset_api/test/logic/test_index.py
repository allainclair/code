# TODO: Create other tests for more complex flows. ex: create -> get -> update -> delete
from pytest import fixture

from logic.index import IndexLogic


from test.fixture.database import engine
from test.model_db.fixture_index import (
    index_1,
    index_1_repeated,
    index_2)


@fixture
def index_logic(engine):
    return IndexLogic(engine)


class TestAssetLogic:
    def test_create(self, index_logic, index_1, index_2):
        assert index_logic.create(index_1)
        assert index_logic.create(index_2)

    def test_create_but_fails_due_to_repeated_index(
            self, index_logic, index_1, index_1_repeated):
        assert index_logic.create(index_1)
        assert not index_logic.create(index_1_repeated)
        assert not index_1_repeated.saved

    def test_delete_ok(self, index_logic, index_1):
        assert index_logic.create(index_1)
        assert index_logic.delete(index_1.id) == index_1

    def test_delete_not_found(self, index_logic):
        to_not_find_id = 9999
        assert not index_logic.delete(to_not_find_id)

    def test_get_all(self, index_logic, index_1, index_2):
        assert index_logic.create(index_1)
        assert index_logic.create(index_2)

        instances = index_logic.get_all()
        assert len(instances) == 2
        assert index_1 in instances and index_2 in instances

    def test_get_not_found(self, index_logic):
        assert index_logic.get(10) is None

    def test_get_ok(self, index_logic, index_1):
        assert index_logic.create(index_1)
        assert index_logic.get(1) == index_1

    def test_update_ok(self, index_logic, index_1):
        assert index_logic.create(index_1)
        current_id = index_1.id
        index_1.id = 1000
        assert index_logic.update(current_id, index_1) == index_1

    def test_update_not_found(self, index_logic, index_1):
        to_not_find_id = 9999
        assert not index_logic.update(to_not_find_id, index_1)
