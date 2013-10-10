twitter-analytics
=================

### Analysis/Visualisation of Tweets 

#### Dependencies
* [Tweepy](https://github.com/tweepy/tweepy) ( Twitter API for python )
* [Logstash](http://logstash.net/) ( including Elastic-Search and Kibana )

#### Basic Idea
    Twitter-->Tweepy-->File (Tweets as Json)-->LogStash-->ElasticSearch-->Kibana
Logstash actually seems to have an input plugin for Twitter but I couldn't make it work in OSX as it uses some native libraries (which is no longer supported by JRuby).
    
#### Setup 
(I am assuming OSX but should be the similar for other Unix variants )

1. I recommend creating an isolated virtual environment for python before installing Tweepy. Go through [this](https://pypi.python.org/pypi/virtualenv) and have it installed in your user area.
2. Install tweepy ( inside the virtualenv you just created )
    `pip install tweepy`
     
3. We will use Twitter's [Streaming API](https://dev.twitter.com/docs/streaming-apis) to access the tweets. 
4. In order to use it, we need to  get the following information
 * Consumer Key
 * Consumer Secret
 * Access Token 
 * Access Token Secret
  
Follow the instructions [here](https://dev.twitter.com/docs/auth/tokens-devtwittercom) to setup a Twitter 'Application' and get this information.

5. I have included the simple wrapper around Tweepy to get the tweets and write them into a file. 
   Update tweepy/oauth.token with the 4 pieces of information.
   
6. Run Tests.py and redirect the output to a file.
    `python Tests.py | tee tweets`
    
7. Once we confirm that the tweets are being written to the file, all that needs to be done is to run Logstash with embedded elastic search server.

8. Go through [Logstash documentation](http://logstash.net/docs/1.2.1/tutorials/getting-started-simple) to learn how to setup logstash. Update "logstash/logstash.conf" with the full path of file where the tweets are being written and use it to start up logstash in standalone mode.

9. That's it. Open up your browser and point to http://localhost:9292 and play around with Kibana.



    