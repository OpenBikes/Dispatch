import os

from dotenv import load_dotenv, find_dotenv


# Load the `.env` file at the root of the repository
load_dotenv(find_dotenv())

DEBUG = True
SECRET_KEY = 'secret!'

REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = int(os.environ.get('REDIS_PORT'))
REDIS_DB_NBR = int(os.environ.get('REDIS_DB_NBR'))
