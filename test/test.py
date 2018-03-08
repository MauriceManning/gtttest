import pymongo
import logging

from pymongo import MongoClient

logging.basicConfig(filename='example.log',level=logging.INFO)

client = MongoClient()

db = client['gtt']

collection = db['test-collection']

post = {"foo": "bar"}
post_id = db.posts.insert_one(post)
logging.info('inserted one doc: ' + str(post_id) )
print('inserted one doc: ' + str(post_id) )
