import os

from pymongo import MongoClient

MONGO_HOST = os.getenv('MONGO_HOST')
# MONGO_PORT = os.environ.get('MONGO_PORT')

connect = MongoClient(
    host=MONGO_HOST,
    port=27017,
    unicode_decode_error_handler='ignore'
)

image_db = connect['image-database']
