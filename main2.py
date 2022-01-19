import tweepy
import configparser
import pandas as pd

config = configparser.ConfigParser()
config.read('config.ini')

consumer_key = 
consumer_secret = 
key = 
secret = 

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
