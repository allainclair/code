from os import getenv

from dotenv import load_dotenv

load_dotenv()

email = getenv('EMAIL')
password = getenv('PASSWORD')
