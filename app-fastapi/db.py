from pymongo import MongoClient


connect = MongoClient(
    host='localhost',
    port=27017,
    unicode_decode_error_handler='ignore'
)

image_db = connect['image-database']
image_collection = image_db['images']
