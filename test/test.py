import pymongo
import psycopg2
import logging
import pprint
from datetime import datetime
import os

from apscheduler.schedulers.blocking import BlockingScheduler

from pymongo import MongoClient


# configure the logger to use common file for all modules.
logging.basicConfig(filename='/code/logs/gtt.log',level=logging.INFO)

# connect to the mongodb repository
def mongoconnect():
    client = MongoClient('mongodb://mongodb:27017/')
    db = client['gtt']
    db.authenticate('gtt', 'gtt123')
    return client, db

# list all collections in mongodb minus system collections
def mongolistcollections():
    #list existing collections
    print( 'collections: ' + str(mongodb.collection_names(include_system_collections=False) ) )
    testcollection = mongodb.testcollection
    posts = mongodb.posts

# create two docs into the mongodb test collection    
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

# read all docs in the mongdb test collection    
def mongoretrieve():
    # retrieve all docs in collection
    print('list testcollection')
    for doc in mongodb.testcollection.find():
        pprint.pprint( doc )

    #print('list posts')
    #for doc in posts.find({}):
    #    pp.pprint( doc )

# connect to the postgres repository
def postgresconnect():    

    global postgresconn
    # test connection to postgres
    try: 
        import time
        time.sleep(7)
        postgresconn = psycopg2.connect(database='gtt', user='gtt', password='gtt123', host='pgdb')
        #conn = psycopg2.connect(user='posgres', password='password123', host='pgdb')
        #cursor = conn.cursor()
        logging.info('connected to postgres')
    except:
        logging.info('connect to postgres failed')


# create a test table in postgres
def createpgtable():
    try: 
        logging.info('create postgres test table')
        cursor = postgresconn.cursor()
        postgresconn.autocommit = True
        cursor.execute("CREATE TABLE test(id INTEGER PRIMARY KEY, name VARCHAR(20),  description VARCHAR(100))")
        logging.info('create postgres test table completed')
    except psycopg2.Error as e:
        if postgresconn:
             postgresconn.rollback()
 
        logging.error('Error on table create %s' % e) 


def insertpgtable():
    try:
        logging.info('insert into  postgres test table')
        cursor = postgresconn.cursor()
        postgresconn.autocommit = True
        cursor.execute( "INSERT INTO test VALUES (1, 'foo', 'bar')" )
        logging.info('insert into  postgres test table completed.')
    except psycopg2.Error as  e:
        if postgresconn:
            postgresconn.rollback()
             
        logging.error('Error on table insert %s' % e)    


def deletepgtable():
    try:
        logging.info('cleanup  postgres test table')
        cursor = postgresconn.cursor()
        postgresconn.autocommit = True
        cursor.execute("DELETE FROM test WHERE id=1")
        logging.info('cleanup  postgres test table completed.')
    except psycopg2.Error as e:
        if postgresconn:
            postgresconn.rollback()

        logging.error('Error on table insert %s' % e)


    
if __name__ == '__main__':
    
    global mongodb
    
    # initial mongodb tests
    import time
    time.sleep(7)
    mongoclient, mongodb = mongoconnect()
    mongolistcollections()
    mongotestinsert()
    
    # test connection to postgres
    postgresconnect()
    createpgtable()
    insertpgtable()
    deletepgtable()
    
    scheduler = BlockingScheduler()
    scheduler.add_job(mongoretrieve, 'interval', seconds=3)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
