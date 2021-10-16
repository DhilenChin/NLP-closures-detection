import spacy
from spacy import displacy
from google.cloud import storage
import os

class begin_end:
    #Structure for begin and end
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        
class tweet_info:
    #Structure to store relevant information from a tweet, used as output in most of the functions
    def __init__(self, content, datetime, tweet_id, in_reply_to_status_id, quoted_status_id, road_name, closure, extra_closure, time, direction, isclosed, solved, coordinates, docs, cause):
        self.content = content
        self.datetime = datetime
        self.tweet_id = tweet_id
        self.in_reply_to_status_id = in_reply_to_status_id	
        self.quoted_status_id = quoted_status_id
        self.road_name = road_name
        self.closure = closure 
        self.extra_closure = extra_closure
        self.time = time
        self.direction = direction
        self.isclosed = isclosed
        self.solved = solved
        self.coordinates = coordinates
        self.docs = docs
        self.cause = cause

class labelling_tweets:
    #Class that labels the tweet with NER labels
    def __init__(self, output= None,
                #List of entitiy labels
                road_name = 'ROAD_NAME', 
                begin_closure = 'BEGIN_CLOSURE', 
                extra_begin_closure = 'EXTRA_BEGIN_CLOSURE',
                end_closure = 'END_CLOSURE', 
                extra_end_closure = 'EXTRA_END_CLOSURE', 
                begin_time = 'BEGIN_TIME', 
                end_time = "END_TIME", 
                direction = "DIRECTION", 
                closure = "CLOSURE",
                solved =  "SOLVED",
                cause = "CAUSE"):
                
                self.output = output
                #store the labels as attributes
                self.road_name = road_name
                self.begin_closure = begin_closure
                self.extra_begin_closure = extra_begin_closure
                self.end_closure = end_closure
                self.extra_end_closure = extra_end_closure
                self.begin_time= begin_time
                self.end_time = end_time
                self.direction = direction
                self.closure = closure
                self.solved = solved
                self.cause = cause
    
    def download_NLP_model(self, bucket_name):
        #Download the NLP model from Google Cloud Storage
        print("Begin downloading the nlp model")
        output_dir = './app/NER/nlp_model/'
        try:
            os.mkdir(output_dir)
            storage_client = storage.Client()
            bucket = storage_client.get_bucket(bucket_name)
            blobs = bucket.list_blobs()  # Get list of files
            for blob in blobs:
                dl_dir = output_dir
                list_of_prefix = blob.name.split("/")
                for n in range(len(list_of_prefix) - 1):
                    try:
                        path = os.path.join(dl_dir, list_of_prefix[n])
                        os.mkdir(path)
                        dl_dir = dl_dir + list_of_prefix[n]
                    except FileExistsError:
                        dl_dir = dl_dir + list_of_prefix[n]
                blob.download_to_filename(output_dir + blob.name)
        except FileExistsError:
            pass
            
        print("Finished downloading the nlp model")

    def NER(self, text):
        #passing text into NER model
        nlp = spacy.load('./app/NER/nlp_model')
        doc = nlp(text)
        return doc


    def visualising_entity(self, text):
        #dsiplaying the Entity Labels on localhost:5000
        doc = self.NER(text)
        colors = {"BEGIN_TIME": "linear-gradient(90deg, dodgerblue, deepskyblue)", 
                "END_TIME": "linear-gradient(90deg, dodgerblue, deepskyblue)", 
                "BEGIN_CLOSURE": "linear-gradient(90deg, #aa9cfc, #fc9ce7)",
                "END_CLOSURE" : "linear-gradient(90deg, #aa9cfc, #fc9ce7)",
                "DIRECTION":"linear-gradient(90deg, lavender, lavenderblush)",
                "ROAD_NAME": "linear-gradient(90deg, aqua, aquamarine)",
                "CLOSURE":"linear-gradient(90deg, cornflowerblue, cyan)",
                "SOLVED":"linear-gradient(90deg, cornflowerblue, cyan)",
                "CAUSE":"linear-gradient(90deg, lightpink, lavenderblush)",
                "EXTRA_BEGIN_CLOSURE":"linear-gradient(90deg, royalblue, paleturquoise)",
                "EXTRA_END_CLOSURE":"linear-gradient(90deg, royalblue, paleturquoise)"}
        options = {"ents": ["BEGIN_TIME", "END_TIME", "BEGIN_CLOSURE", "END_CLOSURE", "ROAD_NAME", "DIRECTION", "CLOSURE","SOLVED", "CAUSE", "EXTRA_BEGIN_CLOSURE","EXTRA_END_CLOSURE"], "colors": colors}
        
        return displacy.serve(doc, style= 'ent', options = options)

    def labelling_tweets_with_NER(self, content, datetime, tweet_id, in_reply_to_status_id, quoted_status_id):
        #Main function in this class
        #Save the result in self.output, which is a tweet_info object
        tweet = tweet_info(content= content, 
                            datetime= datetime,
                            tweet_id= tweet_id,
                            in_reply_to_status_id=in_reply_to_status_id,
                            quoted_status_id=quoted_status_id,
                            road_name=[],
                            closure=begin_end(begin = [],end = []),
                            extra_closure=begin_end(begin = [],end = []),
                            time=begin_end(begin = [], end=[]),
                            direction= [],
                            isclosed=[],
                            solved=[],
                            coordinates=begin_end(begin = [], end = []),
                            docs=[],
                            cause=[])
            
        doc = self.NER(tweet.content)
        tweet.docs = [ent for ent in doc.ents]
        list_of_ent_label = [ent.label_ for ent in tweet.docs]
        if list_of_ent_label.count(self.road_name) > 1 and list_of_ent_label.count(self.begin_closure) > 1 and list_of_ent_label.count(self.end_closure) > 1:
            #For tweets that contain more than one information, this is to orgnise the information so that there would be same amount of information of each closure
            n = 0
            while True:
                try:
                    if tweet.docs[n].label_ == self.end_closure and tweet.docs[n+1].label_ == self.road_name:
                        for j in range(2):
                            tweet.docs.insert(n+1+j, tweet.docs[n-5+j])
                    elif tweet.docs[n].label_ == self.end_closure and tweet.docs[n+1].label_ == self.direction:
                        for j in range(3):
                            tweet.docs.insert(n+1+j, tweet.docs[n-5+j])
                    elif tweet.docs[n].label_ == self.end_closure and tweet.docs[n+1].label_ == self.begin_closure:
                        for j in range(4):
                                tweet.docs.insert(n+1+j, tweet.docs[n-5+j])
                    n+=1
                except:
                    break

        for ent in tweet.docs:
            if ent.label_ == self.road_name:
                tweet.road_name.append(ent.text)
            elif ent.label_ == self.begin_closure:
                tweet.closure.begin.append(ent.text) 
            elif ent.label_ == self.end_closure:
                tweet.closure.end.append(ent.text)
            elif ent.label_ == self.extra_begin_closure:
                tweet.extra_closure.begin.append(ent.text) 
            elif ent.label_ == self.extra_end_closure:
                tweet.extra_closure.end.append(ent.text) 
            elif ent.label_ == self.begin_time:
                tweet.time.begin.append(ent.text)
            elif ent.label_ == self.end_time:
                tweet.time.end.append(ent.text)
            elif ent.label_ == self.direction:
                tweet.direction.append(ent.text)
            elif ent.label_ == self.closure:
                tweet.isclosed.append(ent.text)
            elif ent.label_ == self.solved:
                tweet.solved.append(ent.text)
            elif ent.label_ == self.cause:
                tweet.cause.append(ent.text)
        
        self.output = tweet
