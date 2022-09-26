from os import getenv

from db.start import start


engine = start(getenv('DB_FILE_PATH'))
