from pymongo import MongoClient


connect = MongoClient(host='localhost', port=27017)

image_db = connect['image-database']
image_collection = image_db['images']
