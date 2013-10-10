import json


class TweetTransformer(object):
    def __init__(self):
        pass

    def getUrls(self,tweet):
        urls = []
        if tweet.entities.has_key("urls"):
            for url in tweet.entities["urls"]:
                urls.append(url['expanded_url'])
        return urls

    def getMentions(self,tweet):
        mentions = []
        if tweet.entities.has_key("user_mentions"):
            for um in tweet.entities["user_mentions"]:
                mentions.append(um['screen_name'])
        return mentions

    def getHashTags(self,tweet):
        hashtags = []
        if tweet.entities.has_key("hashtags"):
            for ht in tweet.entities["hashtags"]:
                hashtags.append(ht['text'])
        return hashtags


    def transformTweet(self,tweet):
        tt = dict()
        #The Author
        tt['user.screen_name'] = tweet.user.screen_name
        tt['user.name'] = tweet.user.name
        tt['user.location'] = tweet.user.location
        tt['user.lang'] = tweet.user.lang
        tt['user.friends_count'] = tweet.user.friends_count
        tt['user.followers_count'] = tweet.user.followers_count
        tt['user.description'] = tweet.user.description
        tt['user.statuses_count'] = tweet.user.statuses_count

        #The Tweet
        tt['created_at'] = unicode(tweet.created_at)
        tt['hashtags'] = self.getHashTags(tweet)
        tt['urls'] = self.getUrls(tweet)
        tt['mentions'] = self.getMentions(tweet)
        tt['favorite_count'] = tweet.favorite_count
        tt['lang'] = tweet.lang
        tt['retweet_count'] = tweet.retweet_count
        tt['place'] = tweet.place
        tt['text'] = tweet.text
        return json.dumps(tt)