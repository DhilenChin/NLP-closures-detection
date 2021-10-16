from tqdm import tqdm
import spacy
from spacy.tokens import DocBin
import ast

nlp = spacy.blank("en") # load a new spacy model
db = DocBin() # create a DocBin object

def spacy_converter(input_file_directory ='./app/NER/my_training_data.txt', output_folder_directory = './app/NER', output_file_name = 'my_training_data'):
    f = open(input_file_directory)
    x = f.read()
    DATA = ast.literal_eval(x)
    for text, annot in tqdm(DATA): # data in previous format
        doc = nlp.make_doc(text) # create doc object from text
        ents = []
        for start, end, label in annot["entities"]: # add character indexes
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
        doc.ents = ents # label the text with the ents
        db.add(doc)

    db.to_disk(output_folder_directory + '/'+ output_file_name + ".spacy") # save the docbin object


spacy_converter()