import oauth2 as oauth
import urllib.request as urllib
import json
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

with open('config.json', 'r') as f:
    config = json.load(f)

api_key = config['consumer_key']
api_secret = config['consumer_secret']
access_token_key = config['access_token']
access_token_secret = config['access_token_secret']

_debug = 0

oauth_token = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"

http_handler = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the credentials above.
'''


def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())


def twitterreq(url, method, parameters):
    req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                                token=oauth_token,
                                                http_method=http_method,
                                                http_url=url,
                                                parameters=parameters)

    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

    headers = req.to_header()

    if http_method == "POST":
        encoded_post_data = req.to_postdata()
    else:
        encoded_post_data = None
        url = req.to_url()

    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)

    response = opener.open(url, encoded_post_data)

    return response


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # print(status.text)
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


def fetchsamples():
    # attempt authentication
    # try:
    # create OAuthHandler object
    auth = OAuthHandler(api_key, api_secret)
    # set access token and secret
    auth.set_access_token(access_token_key, access_token_secret)
    # create tweepy API object to fetch tweets
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=auth, listener=myStreamListener)
    myStream.filter(track=['Donald Trump'])


if __name__ == '__main__':
    fetchsamples()
