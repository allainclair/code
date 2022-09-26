from fastapi import FastAPI

from router import asset

app = FastAPI()
app.include_router(asset.router)


# Indexes
#
# @app.post(f'/{INDEXES}')
# def create_index(index: Index):
#     print()
#     ic(index)
#     ic(type(index))
#     if index_create(index):
#         return index
#     else:
#         raise HTTPException(
#             status_code=INDEX_ALREADY_EXISTS.status_code,
#             detail=INDEX_ALREADY_EXISTS.detail,
#         )
#
#
# @app.get(f'/{INDEXES}')
# def get_indexes():
#     # We need to handle database errors in the future.
#     indexes = index_get_all()
#     ic(indexes)
#     return indexes
#
#
# @app.get(f'/{INDEX}/{{index_id}}', response_model=Index)
# def get_index(index_id: int):
#     index = index_get(index_id)
#     if index:
#         return index
#     else:
#         raise HTTPException(
#             status_code=INDEX_NOT_FOUND.status_code,
#             detail=INDEX_NOT_FOUND.detail,
#         )
#
#
# @app.delete(f'/{INDEX}/{{index_id}}', response_model=Index)
# def update_index(index_id: int):
#     index = index_delete(index_id)
#     if index:
#         return index
#     else:
#         raise HTTPException(
#             status_code=INDEX_NOT_FOUND.status_code,
#             detail=INDEX_NOT_FOUND.detail,
#         )
#
#
# @app.put(f'/{INDEX}/{{index_id}}', response_model=Index)
# def update_index(index_id: int, index: Index):
#     index = index_update(index_id, index)
#     if index:
#         return index
#     else:
#         raise HTTPException(
#             status_code=INDEX_NOT_FOUND.status_code,
#             detail=INDEX_NOT_FOUND.detail,
#         )
