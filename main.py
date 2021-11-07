import tweepy

consumer_key = "m63opE9m9xAMm0vA1mWDNnsGu"
consumer_secret = "EoRZGFnlIXtVqbG6kk3c7PzmseJV7IILYq0Uyopq5BevSXkdQ1"
key = "1457353798452645899-XIwG6gfrRp6pRqAMpISBKeEVuC7nEC"
secret = "8RFGXmeRtSLRdBrtDaMExofsPQ2tJqCjOXvHntt4KQKeD"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
api.update_status('this is my demo')

tweets = api.mentions_timeline()


for tweet in tweets:
    if '#swag' in tweet.text.lower():
        print(str(tweet.id)+ ' - ' + tweet.text)