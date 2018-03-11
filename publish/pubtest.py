#!/usr/bin/env python


from birdy.twitter import UserClient
import json
import time
import datetime
import logging


logging.debug( 'test publish to GnuSocial')

# get the credentials for this gene
#client = UserClient(acctCredentials.consumerkey, acctCredentials.consumersecret, acctCredentials.accesstoken, acctCredentials.accesstokenseecret)
client = UserClient('537143b467af36c43ba066238b88c915', 'e62fd6b54f04b65b4790737b493a23be', acctCredentials.accesstoken, acctCredentials.accesstokenseecret)

response = client.api.statuses.update.post(status='test this publish')

logging.info( 'post_tweet post id: %s', response.data.id)
print ("response.data.entities : {0}".format(response.data.entities))
print ("created at: {0}".format(response.data.status))
