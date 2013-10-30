#This test posts messages to my Twitter account


##Install Twitter module: https://code.google.com/p/python-twitter/
import twitter

## Get your authentication from https://dev.twitter.com/
mytwitteraccount = twitter.Api(consumer_key='####', consumer_secret='###', access_token_key='4###', access_token_secret='####')
#



status=mytwitteraccount.PostUpdates('My first API call using Python -- Borris says: "I am invincible!!!')
