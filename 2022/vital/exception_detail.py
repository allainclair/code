from collections import namedtuple

ExceptionDetail = namedtuple('ExceptionDetail', ['status_code', 'detail'])

MALFORMED_START_OR_END_DATE = ExceptionDetail(400, 'Start or end date are malformed')
NO_AVAILABLE_DATA = ExceptionDetail(204, 'No available data for the time period')
