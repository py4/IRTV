import os
import sys

import tweepy


auth = tweepy.auth.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SERCRET'))
auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_SECRET'))
api = tweepy.API(auth)
