import json
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

# Load config file
with open('config.json', 'r') as f:
    config = json.load(f)

# Set configuration parameters from config file
api_key = config['consumer_key']
api_secret = config['consumer_secret']
access_token_key = config['access_token']
access_token_secret = config['access_token_secret']


# Function to clean tweet text
def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())


# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # create TextBlob object of passed tweet text
        print(clean_tweet(status.text).encode('utf-8'))
        analysis = TextBlob(clean_tweet(status.text))
        # set sentiment
        # if analysis.sentiment.polarity > 0:
        #     print('positive')
        # elif analysis.sentiment.polarity == 0:
        #     print('neutral')
        # else:
        #     print('negative')

    def on_error(self, status_code):
        print(status_code)


# Function to get tweets with the help of Tweepy API
def fetchsamples():
    auth = OAuthHandler(api_key, api_secret)
    # set access token and secret
    auth.set_access_token(access_token_key, access_token_secret)
    # create tweepy API object to fetch tweets
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=auth, listener=myStreamListener)
    myStream.filter(track=['Donald Trump'])


if __name__ == '__main__':
    fetchsamples()
