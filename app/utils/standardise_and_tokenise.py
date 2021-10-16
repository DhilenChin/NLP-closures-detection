from nltk.tokenize import RegexpTokenizer

def standardise(text):
    #Standardising words by removing unecessary symbols
    text = text.replace(r"http\S+", "")
    text = text.replace(r"http", "")
    text = text.replace(r"@\S+", "")
    text = text.replace(r"[^A-Za-z0-9(),!?@\'\`\"\_\n]", " ")
    text = text.replace(r"@", "at")
    text = text.lower()
    return text


def standardise_and_tokenise(df, text_field):
    #tokenising text and store in a column of a dataframe
    cleaned_list = [standardise(text) for text in df[text_field]]
    df['clean'] = cleaned_list
    
    tokenizer = RegexpTokenizer(r'\w+')
    df["tokens"] = df[text_field].apply(tokenizer.tokenize)

    return df