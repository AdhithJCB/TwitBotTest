import tweepy
import configparser
import pandas as pd

config = configparser.ConfigParser()
config.read('config.ini')

consumer_key = "MNDULjLgFcChPni7Iqr7M8xSl"
consumer_secret = "vdAf7cgxiR6K0WGWt6K47kZwgPe8kZvvlODwhPNMlv6FIfBS6J"
key = "1457353798452645899-NSXAmmlrVjeEf104Otxo2R0hhxP0Dl"
secret = "voYjNfMuHKqP4lSXbWVNXBc4HHgzAm7w14ChQ5B0fnG3B"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

# create dataframe
columns = ['Time', 'User', 'Tweet']
data = []
for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

df = pd.DataFrame(data, columns=columns)

df.to_csv('tweets2.csv')