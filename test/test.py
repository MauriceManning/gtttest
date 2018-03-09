import pymongo
import psycopg2
import logging
import pprint

from pymongo import MongoClient

logging.basicConfig(filename='example.log',level=logging.INFO)

client = MongoClient('mongodb://mongodb:27017/')
db = client['ingestdb']
db.authenticate('gtt', 'gtt123')

#list existing collections
print( 'collections: ' + str(db.collection_names(include_system_collections=False) ) )
testcollection = db.testcollection
posts = db.posts

#test insert into mongodb
post1 = {"foo": "bar"}
post2 = {"foo2": "bar2"}
post_id1 = db.testcollection.insert_one(post1).inserted_id
logging.info('inserted one doc: ' + str(post_id1) )
print('inserted one doc: ' + str(post_id1) )

post_id2 = db.testcollection.insert_one(post2).inserted_id
logging.info('inserted two doc: ' + str(post_id2) )
print('inserted two doc: ' + str(post_id2) )

#pp = pprint.PrettyPrinter(width=41, compact=True)

# retrieve all docs in collection
print('list testcollection')
for doc in testcollection.find():
    pprint.pprint( doc )

#print('list posts')
#for doc in posts.find({}):
#    pp.pprint( doc )

# test connection to postgres
try: 
    import time
    time.sleep(7)
    conn = psycopg2.connect(database='accounts', user='gtt', password='password123', host='pgdb')
    #conn = psycopg2.connect(user='posgres', password='password123', host='pgdb')
    #cursor = conn.cursor()
    print('connected to postgres')
except:
    print('postgres connect failed.')

print ('end')

    

