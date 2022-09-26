from logging import getLogger

from sqlalchemy.exc import IntegrityError

from model_db.index import Index
from model_db.operation import (
    delete_by_id,
    save_and_refresh,
    select_all,
    select_first_by_id,
    update_and_refresh_by_id)

logger = getLogger(__name__)


class IndexLogic:
    def __init__(self, engine):
        self.engine = engine

    def create(self, new_index: Index) -> bool:
        try:
            return save_and_refresh(self.engine, new_index)
        except IntegrityError:
            logger.exception(
                'IntegrityError error. Please check the Index Model constraints')
            return False

    def get(self, index_id: int) -> Index | None:
        return select_first_by_id(self.engine, Index, index_id)

    def get_all(self) -> list[Index]:
        return select_all(self.engine, Index)

    def delete(self, index_id: int) -> Index | bool:
        return delete_by_id(self.engine, Index, index_id)

    def update(self, index_id_to_update: int, new_index: Index) -> Index | bool:
        return update_and_refresh_by_id(
            self.engine, Index, index_id_to_update, new_index)
