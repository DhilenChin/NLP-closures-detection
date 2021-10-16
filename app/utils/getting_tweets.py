import tweepy
import pandas as pd
import os 
import json
f = open(os.environ["TWITTER_AUTH"])
keys = json.load(f)
consumer_key= keys["consumer_key"]
consumer_secret= keys["consumer_secret"]
access_token= keys["access_token"]
access_token_secret=keys["access_token_secret"]
    
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def tweet_extraction(acc_name, num_of_tweets):
    #Obtain a pandas.dataframe of tweets of a single twitter account
    tweets = tweepy.Cursor(api.user_timeline, screen_name=acc_name, include_rts = False, tweet_mode = 'extended').items(num_of_tweets)
    id_list = [tweet.id for tweet in tweets]
    status_list = [api.get_status(ids, tweet_mode = "extended") for ids in id_list]
    df = organise_tweets_in_df(status_list)
    return df

def keywords_querying(keywords, num_of_tweets):
    #Obtain a pandas.dataframe of tweets that contain queried keywords
    query = keywords
    searched_tweets = tweepy.Cursor(api.search, q=query, lang = 'en', count = num_of_tweets).items(num_of_tweets)
    id_list = [tweet.id for tweet in searched_tweets]
    status_list = [api.get_status(ids, tweet_mode = 'extended') for ids in id_list]
    df = organise_tweets_in_df(status_list)
    return df

def organise_tweets_in_df(status_list):
    #Organising list of statuses into dataframe
    df = pd.DataFrame(list())
    tweet_list = []
    for status in status_list:
        try:
            tweet_list.append(status.retweeted_status.full_text.encode('cp1252', 'ignore').decode('utf-8','ignore'))
        except:
            tweet_list.append(status.full_text.encode('cp1252','ignore').decode('utf-8','ignore'))
    date_list = [status.created_at for status in status_list]

    df['Date time'] = date_list
    df['Content'] = tweet_list
    return df