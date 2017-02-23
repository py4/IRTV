import os
import sys

import tweepy


auth = tweepy.auth.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
