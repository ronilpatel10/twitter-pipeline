import tweepy
import panads as pd 
import json 
from datetime import datetime 
import s3fs 

access_key ="eXabPMFu8L09dGxv3uWcdj8Dm"
access_secret ="CKI4grMAmlJrM8tlaxpZsORhJWHSIHlab0nxKp1uID6iNYURBk"
consumer_key="1260876362-P1hAwcVfTJdYy95Ani1OBNZLmzPCKmf5zUa5xre"
consumer_secret="Z4BWs6JYLqXWTgPBgx5Iqv97RY0wsLAZD0h9iZmyf5KpW"

#twitter auth
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token = tweepy.OAuthHandler(consumer_key, consumer_secret)

#Creating API object
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name = "BillGates", 
                           count = 200, 
                           include_rts = False, 
                           #keeps full_text otherwise only first 140 words will be extracted
                           tweet_mode="extended")

