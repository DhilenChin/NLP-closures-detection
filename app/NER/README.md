# spaCy Named Entities Recognition (NER)
Using spaCy library to train a transforemers-based pipline for named entitires recognition.

## Training steps
1. Save a list of tweets in a `.txt` file. Make sure to save it as one tweet per line in the file.
    * In `getting_tweets.py`, there are `tweet_extraction` and `keywords_qurying` fucntions that can obtain a list of tweets in a `pandas.Dataframe` object. This might be useful to obtain large number of tweets.
2. Use this [repository](https://github.com/ManivannanMurugavel/spacy-ner-annotator) to label your tweets with your self-defined entities and obtain a `.json` and `.txt` files of training data in the spacy format. Name the files `my_training_data.json` and `my_training_data.txt`. Copy both files into `./app/NER`. 
3. Run the `spacy_converter` python function to convert the `my_training_data.txt` file into a `.spacy` file. Name the file `my_training_data.spacy` (This is done by default if you do not pass any arguments into the `spacy_converter` function)
4. At the [spacy website](https://spacy.io/usage/training), select ner, GPU(transformer), and accuracy to generate a `base_config.cfg`. Copy this file into `./app/NER/config_files`. In terminal, in the `./app/NER` directory, run 
```
python -m spacy init fill-config ./config_files/base_config.cfg ./config_files/config.cfg
```
5. Remain in the `./app/NER` directory in terminal. Run
```
python -m spacy train ./config_files/config.cfg --output ./nlp_model_output --paths.train ./directory/to/your/training/file.spacy --paths.dev ./directory/to/your/training/file.spacy --gpu-id 0
```
* Running on GPU might not be possible for some cases, check **Using CPU** to train with CPU instead.
6. The trained models should be stored in `nlp_model_output` folder. There will be two models in this folder `model-last` and `model-best`. Use `model-last` for most of the cases.
7. To pass text into the model
```python
import spacy
nlp = spacy.load('./app/NER/nlp_model_output/model-last')
doc = nlp('Your text here')
for ent in doc.ents:
    print("Entity text is: {}, entity label is: {}".format(ent.text, ent.label_))
```
## Using CPU
* The training uses GPU and takes some time. Training with GPU uses PyTorch and CUDA for the transformers model. Read [here](https://spacy.io/usage/embeddings-transformers) under **Using tansformer models** for more information. 
* To train a ligter model that is not based on transformers, select CPU instead of GPU(transformer) for the `base_config.cfg` in step 4, and remove `--gpu-id 0` in step 5 to train the model on CPU instead. 

## Testing
After training the model, run a test to see the metrics score.
1. Create testing data the same way training data was created. (step 1,2 and 3 in training)
2. Named the files `my_testing_data.json`, `my_testing_data.txt` and `my_testing_data.spacy`. (Change the arguments in `spacy_converter` accordingly).
3. In terminal, in `./app/NER` directory, run
```
python -m spacy evaluate ./nlp_model_output/model-last ./my_testing_data.spacy --output ./NER_metrics.json --gpu-id 0
```
4. The PRF scores of the model is stored in `NER_metrics.json`.