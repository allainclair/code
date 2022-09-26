from pytest import raises
from sqlalchemy.exc import IntegrityError

from model_db.index import Index
from model_db.operation import (
    save_and_refresh,
    select_first_by_id)

from test.fixture.database import engine
from test.model_db.fixture_index import (
    index_1,
    index_1_repeated,
    index_2)


def test_add_index_without_id(engine, index_1):
    assert index_1.id is None
    assert save_and_refresh(engine, index_1)
    assert index_1.saved
    assert select_first_by_id(engine, Index, index_1.id) == index_1


def test_add_index_with_id(engine, index_2):
    id_ = 9999
    index_2.id = id_
    assert save_and_refresh(engine, index_2)
    assert index_2.saved
    assert select_first_by_id(engine, Index, index_2.id) == index_2
    assert index_2.id == id_


def test_add_index_but_fails_due_to_repeated_index_name(
        engine, index_1, index_1_repeated):
    assert save_and_refresh(engine, index_1)
    with raises(IntegrityError):
        assert save_and_refresh(engine, index_1_repeated)

