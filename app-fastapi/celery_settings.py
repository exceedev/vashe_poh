import os

from celery import Celery
from dotenv import load_dotenv

load_dotenv('.env')

RABBIT_BROKER = os.getenv('RABBIT_BROKER')
RABBIT_BACKEND = os.getenv('RABBIT_BACKEND')

app = Celery(
    'app-fastapi',
    broker=RABBIT_BROKER,
    backend=RABBIT_BACKEND
)
