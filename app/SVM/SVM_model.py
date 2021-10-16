from utils.standardise_and_tokenise import standardise
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
import pandas as pd

class SVM_model:
    def __init__(self, df = pd.read_csv("./app/SVM/SVM_data/querying_traffic_related_tweets.csv"), text_title = 'Content', class_label_title = 'class_label'):
        self.df = df
        self.text_title = text_title
        self.class_label_title = class_label_title

    def training(self, C=1.0, kernel = 'linear', degree = 3, gamma = 'auto'):
        list_corpus = self.df[self.text_title].tolist()
        list_labels = self.df[self.class_label_title].tolist()
        #splitting train-test into 80:20
        X_train, X_test, y_train, y_test = train_test_split(list_corpus, list_labels, test_size=0.2, random_state=40)
        
        #Using TF-IDF vectoriser to get vectors representation of the content
        tfidf_vectorizer = TfidfVectorizer()
        X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)

        self.X_train_tfidf = X_train_tfidf
        self.tfidf_vectorizer = tfidf_vectorizer

        X_test_tfidf = self.tfidf_vectorizer.transform(X_test)

        self.X_test_tfidf = X_test_tfidf
        self.y_train = y_train
        self.y_test = y_test
        
        svm_vc = svm.SVC(C, kernel, degree, gamma)
        self.svm_vc = svm_vc
        svm_vc.fit(self.X_train_tfidf, self.y_train)

        y_predicted_SVM = svm_vc.predict(self.X_test_tfidf)

        self.y_predicted = y_predicted_SVM

    def predict(self, content):

        content = [standardise(content)]
        vectorised_content = self.tfidf_vectorizer.transform(content)

        svm_vc = self.svm_vc
        svm_vc.fit(self.X_train_tfidf, self.y_train)

    
        predicted = svm_vc.predict(vectorised_content)
        if predicted[0] == 1:
            return 1

        elif predicted[0] == 0:
            return 0

        elif predicted[0] == 2:
            return 2
