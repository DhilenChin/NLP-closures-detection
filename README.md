# ClosureDetection

Using Natural Language Processing to detect road closures from tweets.

## Running the Program Locally
1. Install the list of dependencies from `requirements.txt`
2. Obtain the twitter developer account authentication information following the steps [here](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api). Store the information in a json file in this format. 
```
{
"consumer_key":"1111", 
"consumer_secret": "2222", 
"access_token": "3333",
"access_token_secret": "4444"
}
``` 
3. Set your environment variable of `TWITTER_AUTH` to the path of your `auth.json`.

4. If you have Google Cloud Account set up, in cmd run
```
kubectl port-forward -n nugraph service/junction-coordinates 8080
```
* To check if you could call the junction-coordinates service locally, head to this [link](http://localhost:8080/?road=M11&junc=10), which should give the coordinates of road M11 and junction J10.

5. Change `print_closure_information` from the arguments to True to see closure information being printed out. 

6. SVM:
    * Using SVM
        * Set `include_SVM` to be True
        * Set `list_of_queries` to obtain tweets with specific keywords.
    * Not using SVM
        * Set `include_SVM` to be False
        * Edit `twitter_accounts.json` to include twitter handles to listen to.
        
7. Run the program.
<br><br>

**Note on grpc**: This program uses two grpc services. If error occurs due to incompatible version of the service, run `get_api.sh` to get the latest version of the API.<br><br>
**Note on Google Cloud Storage**: If you do not have `GOOGLE_APPLCIATION_CREDENTIALS` set up, check [here](https://cloud.google.com/docs/authentication/getting-started?authuser=2#cloud-console) on how to do it.<br><br>
**Note on running on VSCode**: Please install the Python extension in VS code for the imports to work.
<br><br>
## Training a Named Entity Recognition spaCy model
Read the doc at [here](./app/NER)

## Using SVM to classify tweet
Read the doc at [here](./app/SVM)
