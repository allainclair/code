from logging import getLogger

from sqlalchemy.exc import IntegrityError

from model_db.asset import Asset
from model_db.operation import (
    save_and_refresh,
    select_all,
    select_first_by_id)

logger = getLogger(__name__)

from icecream import ic


class AssetLogic:
    def __init__(self, engine):
        self.engine = engine

    def create(self, new_asset: Asset) -> bool:
        try:
            return save_and_refresh(self.engine, new_asset)
        except IntegrityError:
            logger.exception(
                'IntegrityError error. Please check the Asset Model constraints')
            return False

    def get(self, asset_id: int) -> Asset | None:
        return select_first_by_id(self.engine, Asset, asset_id)

    def get_all(self) -> list[Asset]:
        return select_all(self.engine, Asset)
