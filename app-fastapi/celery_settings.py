import os

from celery import Celery
from dotenv import load_dotenv

load_dotenv('.env')

RABBIT_BROKER = os.getenv('CELERY_BROKER_URL')
RABBIT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')

app = Celery(
    'app-fastapi',
    broker=RABBIT_BROKER,
    backend=RABBIT_BACKEND
)
