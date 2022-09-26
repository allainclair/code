from fastapi import (
    APIRouter,
    HTTPException)

from db.main import engine
from router.exception_detail import (
    INDEX_ALREADY_EXISTS,
    INDEX_NOT_FOUND)
from logic.index import IndexLogic
from model_db.index import Index
from router.url_v1 import URL_INDEX

router = APIRouter()
index_logic = IndexLogic(engine)


from icecream import ic


@router.post(f'{URL_INDEX}')
def create_index(index: Index):
    if index_logic.create(index):
        return index
    raise HTTPException(*INDEX_ALREADY_EXISTS)


@router.get(f'{URL_INDEX}', response_model=list[Index])
def get_indexes():
    return index_logic.get_all()


@router.get(f'{URL_INDEX}/{{index_id}}')
def get_index(index_id: int):
    index = index_logic.get(index_id)
    if index is not None:
        return index
    else:
        raise HTTPException(*INDEX_NOT_FOUND)


@router.delete(f'{URL_INDEX}/{{index_id}}')
def delete_index(index_id: int):
    index = index_logic.delete(index_id)
    if index:
        return index
    else:
        raise HTTPException(*INDEX_NOT_FOUND)


@router.put(f'{URL_INDEX}/{{index_id}}')
def update_index(index_id: int, index: Index):
    index = index_logic.update(index_id, index)
    if index:
        return index
    else:
        raise HTTPException(*INDEX_NOT_FOUND)
