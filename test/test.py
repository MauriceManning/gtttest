import pymongo
import psycopg2
import logging
import pprint
from datetime import datetime
import os

from apscheduler.schedulers.blocking import BlockingScheduler

from pymongo import MongoClient

logging.basicConfig(filename='gtt.log',level=logging.INFO)


def mongoconnect():
    client = MongoClient('mongodb://mongodb:27017/')
    db = client['gtt']
    db.authenticate('gtt', 'gtt123')
    return client, db

def mongolistcollections():
    #list existing collections
    print( 'collections: ' + str(mongodb.collection_names(include_system_collections=False) ) )
    testcollection = mongodb.testcollection
    posts = mongodb.posts
    
def mongotestinsert():
    #test insert into mongodb
    post1 = {"foo": "bar"}
    post2 = {"foo2": "bar2"}
    post_id1 = mongodb.testcollection.insert_one(post1).inserted_id
    logging.info('inserted one doc: ' + str(post_id1) )
    print('inserted one doc: ' + str(post_id1) )

    post_id2 = mongodb.testcollection.insert_one(post2).inserted_id
    logging.info('inserted two doc: ' + str(post_id2) )
    print('inserted two doc: ' + str(post_id2) )
    #pp = pprint.PrettyPrinter(width=41, compact=True)
    
def mongoretrieve():
    # retrieve all docs in collection
    print('list testcollection')
    for doc in mongodb.testcollection.find():
        pprint.pprint( doc )

    #print('list posts')
    #for doc in posts.find({}):
    #    pp.pprint( doc )

def postgresconnect():    
    # test connection to postgres
    try: 
        import time
        time.sleep(7)
        conn = psycopg2.connect(database='gtt', user='gtt', password='gtt123', host='pgdb')
        #conn = psycopg2.connect(user='posgres', password='password123', host='pgdb')
        #cursor = conn.cursor()
        print('connected to postgres')
    except:
        logging.info('connect to postgres failed')

    
if __name__ == '__main__':
    
    global mongodb
    
    # initial mongodb tests
    mongoclient, mongodb = mongoconnect()
    mongolistcollections(mongodb)
    mongotestinsert(mongodb)
    
    # test connection to postgres
    postgresconnect()
    
    scheduler = BlockingScheduler()
    scheduler.add_job(mongoretrieve(mongodb), 'interval', seconds=3)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
