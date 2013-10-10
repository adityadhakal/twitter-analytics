#!/usr/bin/env python


import tweepy
import webbrowser


def get_access_token(ckey, csecret):
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth_url = auth.get_authorization_url(signin_with_twitter=True)
    webbrowser.open(auth_url)
    print "If a browser window didn't open goto [{0}]. Authenticate and get PIN".format(auth_url)
    verifier = raw_input('PIN: ').strip()
    return auth.get_access_token(verifier)


def get_oauth(token_file):
    with open(token_file) as tokenfile:
        [CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]=map(lambda x: x.rstrip('\n'),tokenfile.readlines())
    oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    oauth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return oauth

def get_api(token_file="oauth.token"):
    return tweepy.API(get_oauth(token_file))

def get_stream(listener,token_file="oauth.token"):
    return tweepy.streaming.Stream(get_oauth(token_file),listener,secure=True)

if __name__ == "__main__":
    print get_api().friends()
