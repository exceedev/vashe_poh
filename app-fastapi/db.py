import os

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv('.env')

MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = os.getenv('MONGO_PORT')


cluster = AsyncIOMotorClient(f'mongodb://{MONGO_HOST}:{MONGO_PORT}')
database = cluster.image_db
collection = database.images
