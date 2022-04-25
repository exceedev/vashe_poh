import os
# import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
# from pymongo import MongoClient
#
MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = os.getenv('MONGO_PORT')


cluster = AsyncIOMotorClient('mongodb://127.0.0.1:27017')
database = cluster.image_db
collection = database.images

