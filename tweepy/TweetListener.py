
from tweepy.streaming import StreamListener
from pprint import PrettyPrinter
from CounterFactory import CounterFactory
from TweetTransformer import TweetTransformer

class TweetListener(object):
    def __init__(self,name):
        self.filter=None
        self.name=name
    
    def onTweet(self,tweet):
        if (not self.filter) or (not filter.isFilterable(tweet)):
            self.processTweet(tweet)
                
    def processTweet(self,tweet):
        pass
    
class TweetSummaryPrinter(TweetListener):
    def __init__(self):
        TweetListener.__init__(self,"TweetSummaryPrinter")
        
    def processTweet(self,tweet):
        print "Tweeted By: " + tweet.user.name
        print "Text: " + tweet.text
        print '-' * 20


class TweetJsonPrinter(TweetListener):
    def __init__(self,tt):
        TweetListener.__init__(self, "TweetJsonPrinter")
        self.tt = tt

    def processTweet(self, tweet):

        try:
            print self.tt.transformTweet(tweet)
        except:
            pass


class TweetRawPrinter(TweetListener):
    def __init__(self):
        TweetListener.__init__(self,"TweetRawPrinter")
        self.pp = PrettyPrinter(indent=4)
        
    def processTweet(self,tweet):
        print "Raw Tweet: "
        self.pp.pprint(tweet.__dict__)
        print '-' * 20
 
class UserAnalyzer(TweetListener):
    def __init__(self,n=10):
        TweetListener.__init__(self,"UserAnalyzer")
        self.pp = PrettyPrinter(indent=4)
        self.users = {}  #List of users
        self.n = n      #How many users do we store?
        
    def removeMin(self):
        if len(self.users) <= self.n:
            return
        
        minF = min([u.followers_count for u in self.users.values()])
        for name,user in self.users.items():
            if(user.followers_count == minF):
                del self.users[name]

        
    def printUserRaw(self,user):
        print "User: "
        self.pp.pprint(user.__dict__)
        print '-' * 20
    
    def printUserSummary(self,user):
        print u'[screen_name:{0}, location:{1}, followers:{2} ]'.format(user.screen_name,user.location,user.followers_count)
        
    def processTweet(self,tweet):
        user = tweet.user
        #self.printUserRaw(user)
        self.users[user.screen_name]=user
        self.removeMin()
        
        if CounterFactory.getCounter("PrintTopUsers",10).countUp():
            self.printTopUsers()
        
    def printTopUsers(self):
        print "Top Tweeters so far:"
        for user in self.users.values():
            self.printUserSummary(user)
            
        
class TweetRouter(StreamListener):
    def __init__(self):
        StreamListener.__init__(self)
        self.destinations = []

    def on_status(self, status):
        for dest in self.destinations:
            dest.onTweet(status)

    def addDestination(self,dest):
        self.destinations.append(dest)
    
    def removeDestination(self,dest):
        self.destinations.remove(dest)
        
        
