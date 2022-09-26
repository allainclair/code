from fastapi import (
    APIRouter,
    HTTPException)

from db.main import engine
from router.exception_detail import (
    ASSET_ALREADY_EXISTS,
    ASSET_NOT_FOUND)
from logic.asset import AssetLogic
from model_db.asset import Asset
from router.url_v1 import URL_ASSET

router = APIRouter()
asset_logic = AssetLogic(engine)


@router.post(f'{URL_ASSET}')
def create_asset(asset: Asset):
    if asset_logic.create(asset):
        return asset
    raise HTTPException(*ASSET_ALREADY_EXISTS)


@router.get(f'{URL_ASSET}', response_model=list[Asset])
def get_assets():
    return asset_logic.get_all()


@router.get(f'{URL_ASSET}/{{asset_id}}')
def get_asset(asset_id: int):
    asset = asset_logic.get(asset_id)
    if asset is not None:
        return asset
    else:
        raise HTTPException(*ASSET_NOT_FOUND)
