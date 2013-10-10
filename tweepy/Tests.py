#!/usr/bin/env python
# coding=utf-8

from tweepy_auth import get_stream
from TweetListener import *
from TweetTransformer import TweetTransformer
from Signals import handle_signals

import sys

handle_signals()

tr = TweetRouter()
tr.addDestination(TweetJsonPrinter(TweetTransformer()))
stream = get_stream(tr)

#Use this to get tweets from your stream
stream.userstream()

#Use this to get public tweets from a given area (specified by co-ordinates)
#stream.filter(locations=[139.7,35.6,139.8,35.7])

#Use this to get public tweets with a given array of keywords
#stream.filter(track=["roppongi"])
