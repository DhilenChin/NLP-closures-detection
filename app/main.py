import tweepy
from NER.labelling_tweets import labelling_tweets
from SVM.SVM_model import SVM_model
import os
import json 
from streaming_tweets import MyStreamListener
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)
from google.protobuf.timestamp_pb2 import Timestamp
import argparse
os.environ["TWITTER_AUTH"]= "C:/Users/user/Documents/Graphmasters/twitter_auth.json"
def run():
    #Setting arguments from configuration
    parser = argparse.ArgumentParser(description='Arguments to set for main.py')
    parser.add_argument('--address', dest='address', type= str, default='localhost:8080')
    parser.add_argument('--timezone', dest='timezone', type = str, default='Europe/London')
    parser.add_argument('--model_bucket_name', dest='model_bucket_name', type = str, default='closures-detection-nlp-ner-model')
    parser.add_argument('--print_closure_information', dest ='print_closure_information', type= bool, default= True)
    parser.add_argument('--include_SVM', dest = 'include_SVM', type=bool, default= False)
    parser.add_argument('--list_of_queries', dest = 'list_of_queries', type=list, default= ['road', 'closures','traffic', 'blocked', 'closed'])
    args = parser.parse_args()

    #Accesing the environment variable to obtain the twtitter Auth
    f = open(os.environ["TWITTER_AUTH"])
    keys = json.load(f)
    consumer_key= keys["consumer_key"]
    consumer_secret= keys["consumer_secret"]
    access_token= keys["access_token"]
    access_token_secret=keys["access_token_secret"]
    
    #Initialising the Tweepy API 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    #Getting tweet ids of twitter accounts in twitter_accounts.json
    tweeters = open('./app/twitter_accounts.json')
    acc_names = json.load(tweeters)
    list_of_tweeter_ids = [api.get_user(user).id_str for user in acc_names["twitter_accs"]] #list of twitter account ids to listen to
    
    #Download the NLP model from Google Cloud Storage
    download = labelling_tweets()
    download.download_NLP_model(bucket_name=args.model_bucket_name)

    #Initialising the SVM model  
    trained_svm = initialise_SVM(args)

    #Calling the stream listener from tweepy
    calling_stream_lsitener(api, args, trained_svm, list_of_tweeter_ids)

def initialise_SVM(include_SVM):
    if include_SVM == True:
        print("Initialising the SVM model to be used")
        svm = SVM_model()
        trained = svm.training()
        print("Finsihed initialising the SVM model to be used")
        return trained
    else:
        return None

def calling_stream_lsitener(api, args, trained_svm, list_of_tweeter_ids):
    stream_listener = MyStreamListener(api, args, trained_svm)
    stream = tweepy.Stream(auth = api.auth, listener = stream_listener)
    if args.include_SVM == True:
        stream.filter(track=args.list_of_queries)
    else:
        stream.filter(follow=list_of_tweeter_ids)


if __name__ == "__main__":
    timestampnow = Timestamp()
    timestampnow.GetCurrentTime()
    print("time of initialising: {}".format(timestampnow.ToDatetime()))
    print("NLP-closures-detection begin running")
    run()

