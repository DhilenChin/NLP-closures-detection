import tweepy
from NER.labelling_tweets import labelling_tweets
from MAP.matching_coor import matching_coor
from MAP.update_database import update_database, replace_accident

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api, args, svm):
        super().__init__(api=api)
        self.args = args
        self.svm = svm

    accident_list = []
    def on_status(self, status):
        #Whenever there is a new tweet, this funciton is called

        full_status = self.api.get_status(status.id, tweet_mode = "extended")
        tweet_str = full_status.full_text.encode('cp1252','ignore').decode('utf-8','ignore').replace('&amp;', '&')
        print(tweet_str)
        try:
            quoted_status_id = full_status.quoted_status.id
        except AttributeError:
            quoted_status_id = None

        if self.args.include_SVM == True:
            if self.svm.predict(tweet_str) == 0:
                return

        #Labelling the tweets with Named Entities 
        ner = labelling_tweets()
        ner.labelling_tweets_with_NER(  content= tweet_str, 
                                        datetime= full_status.created_at, 
                                        tweet_id=full_status.id, 
                                        in_reply_to_status_id=full_status.in_reply_to_status_id, 
                                        quoted_status_id= quoted_status_id)
        
        #Obtanining coordinates from junction-coordinates:8080
        match_coor = matching_coor(output = ner.output, address= self.args.address)
        match_coor.matching_coor()

        output = match_coor.output

        #Check if the tweet is related to a previous accident tweet.
        for n, accident in enumerate(self.accident_list):
            same_road_closure = accident.output.road_name + accident.output.closure.begin + accident.output.closure.end == output.road_name + output.closure.begin + output.closure.end
            is_related_tweet = accident.output.tweet_id == output.in_reply_to_status_id or accident.output.tweet_id == output.quoted_status_id or same_road_closure
            if is_related_tweet and len(output.solved) != 0:
                print("is related and is solution")
                list_of_closures = replace_accident(output= output, accident=accident)
                for closures in list_of_closures:
                    print(closures.id)
                    print(closures.start_time)
                    print(closures.end_time)
                self.accident_list.pop(n)
                return
        
        if self.args.print_closure_information == True:
            print("road is {}".format(output.road_name))
            print("begin closure is: {}, end closure is {}".format(output.closure.begin, output.closure.end))
            print("begin time is: {}, end time is {}".format(output.time.begin, output.time.end))
            print("begin coor is: {}, end coor is {}".format([(coor.lat, coor.lon) for coor in output.coordinates.begin], [(coor.lat, coor.lon) for coor in output.coordinates.end]))

        # Check if the tweet is about a closure   
        if len(output.isclosed) == 0:
            return

        list_of_closures, accident = update_database(timezone_loc = self.args.timezone, output =match_coor.output)
        
        if accident != None:
            self.accident_list.append(accident)
        
        for closures in list_of_closures:
            print(closures.id)
            print(closures.start_time)
            print(closures.end_time)

    def on_error(self, status_code):
        if status_code == 420:
            return False