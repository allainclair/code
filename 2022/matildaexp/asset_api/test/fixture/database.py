from os import getenv
from subprocess import run

from dotenv import load_dotenv
from pytest import fixture

from db.start import start as db_start

load_dotenv('test/.env')


@fixture
def engine():
    file_path = getenv('DB_FILE_PATH')
    try:
        engine = db_start(file_path)
        yield engine
    finally:
        run(['rm', file_path])
