import numpy 
import torch
import tweepy
import os 

twitter_api_key = os.getenv("TWITTER_API_KEY")
twitter_secret_key = os.getenv("TWITTER_SECRET_KEY")
twitter_access_token = os.getenv("TWITTER_ACCESS_TOKEN")
twitter_secret_token = os.getenv("TWITTER_SECRET_TOKEN")

client = tweepy.Client(
    consumer_key=twitter_api_key,
    consumer_secret=twitter_secret_key,
    access_token=twitter_access_token,
    access_token_secret=twitter_secret_token
)

def make_tweet(text):
    tweet = client.create_tweet(text = text)
    print(f"Tweet posted to timeline: {text}")

client.get_user(username="Cryptocuck18")
client.get_users_tweets()

#make_tweet("test")
