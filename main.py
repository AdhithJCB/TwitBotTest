import tweepy

consumer_key = "CONSUMER KEY"
consumer_secret = "SECRET"
key = "KEY"
secret = "SECRET"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
api.update_status('this is my demo')

tweets = api.mentions_timeline()


for tweet in tweets:
    if '#swag' in tweet.text.lower():
        print(str(tweet.id)+ ' - ' + tweet.text)
