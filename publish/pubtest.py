#!/usr/bin/env python


from birdy.twitter import UserClient
import json
import time
import datetime
import logging
from apscheduler.schedulers.blocking import BlockingScheduler


from birdy.twitter import UserClient  

class GnuClient(UserClient):
    def __init__(self, consumer_key, consumer_secret, access_token=None, access_token_secret=None):
        super(GnuClient, self).__init__(consumer_key, consumer_secret, access_token, access_token_secret)
        self.base_api_url = 'http://172.104.49.249:8000/%s'

    def construct_resource_url(self, path):
        paths = path.split('/')
        return '%s/%s.json' % (self.base_api_url % paths[0], '/'.join(paths[1:]))


def posttweet():
  response = client.api.statuses.update.post(status="dckrtest")
  print('post response: ' + str(response) )
      
if __name__ == "__main__":
    
    global client

    logging.debug( 'test publish to GnuSocial')
    credentials = ("dcb80dabca4abbf7d7ab433e9a664db9",
                   "a788435690cd0249cc85be8dfe3b2a88",
                   "f1f24e064efaf74e1d1fe5ab86044770",
                   "eecd2dd0b03d892fb798ac87ab3f8c26")

    client = GnuClient(*credentials)
    #response = client.api.statuses.update.post(status="Test4")

    
    scheduler = BlockingScheduler()
    scheduler.add_job(posttweet, 'interval', seconds=5)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        print('start scheduler ') 
        scheduler.start()
        
    except (KeyboardInterrupt, SystemExit):
        pass
