#!/usr/bin/env python
import sys, os, time
import tweepy
from keys import * 
# import Keys from keys.py

#Auth With Tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def tweet():
	message=input("tweet: ")
	api.update_status(message)
	time.sleep(15)
if __name__ == "__main__":
	while 1:
		tweet()