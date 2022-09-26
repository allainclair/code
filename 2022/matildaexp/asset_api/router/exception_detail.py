from collections import namedtuple

ExceptionDetail = namedtuple('ExceptionDetail', ['status_code', 'detail'])

ASSET_ALREADY_EXISTS = ExceptionDetail(400, 'Asset already exists')
ASSET_NOT_FOUND = ExceptionDetail(404, 'Asset not found')

INDEX_ALREADY_EXISTS = ExceptionDetail(400, 'Index already exists')
INDEX_NOT_FOUND = ExceptionDetail(404, 'Index not found')
