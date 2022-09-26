from pytest import fixture

from model_db.index import Index


@fixture
def index_1():
    return Index(name='Index 1', value=0.05)


@fixture
def index_1_repeated():
    return Index(name='Index 1', value=0.05)


@fixture
def index_2():
    return Index(name='Index 2', value=0.05)
