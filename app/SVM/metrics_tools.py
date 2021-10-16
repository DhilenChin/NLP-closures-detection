from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report
import numpy as np
import itertools
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import TruncatedSVD
import matplotlib
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

class metrics_tools:
    def get_metrics(self, y_test, y_predicted):  
        # true positives / (true positives+false positives)
        precision = precision_score(y_test, y_predicted, pos_label=None, average='weighted')             
        self.precision = precision
        # true positives / (true positives + false negatives)
        recall = recall_score(y_test, y_predicted, pos_label=None, average='weighted')
        self.recall = recall
        # harmonic mean of precision and recall
        f1 = f1_score(y_test, y_predicted, pos_label=None, average='weighted')
        self.f1 = f1
        # true positives + true negatives/ total
        accuracy = accuracy_score(y_test, y_predicted)
        self.accuracy = accuracy
        
        return print("accuracy = %.3f, precision = %.3f, recall = %.3f, f1 = %.3f" % (accuracy, precision, recall, f1))

    def plot_confusion_matrix(self, y_test, y_predicted, normalize=False, title='Confusion matrix', cmap=plt.cm.winter):
        cm = confusion_matrix(y_test, y_predicted)
        self.cm = cm
        classes = ['Non-closure', 'Closure', 'Unsure']
        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title, fontsize=30)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, fontsize=20)
        plt.yticks(tick_marks, classes, fontsize=20)
    
        fmt = '.2f' if normalize else 'd'
        thresh = cm.max() / 2.

        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, format(cm[i, j], fmt), horizontalalignment="center", 
                 color="white" if cm[i, j] < thresh else "black", fontsize=40)
    
        plt.tight_layout()
        plt.ylabel('True label', fontsize=30)
        plt.xlabel('Predicted label', fontsize=30)
        fig = plt.figure(figsize=(10, 10))
        plt.show()
        return print(cm)
    
    def get_most_important_features(self, X_train, y_train, vectoriser, n =5):
        clf_tfidf = LogisticRegression(C=30.0, class_weight='balanced', solver='newton-cg', multi_class='multinomial', n_jobs=-1, random_state=40)
        clf_tfidf.fit(X_train, y_train)
        index_to_word = {v:k for k,v in vectoriser.vocabulary_.items()}
        classes ={}
        for class_index in range(clf_tfidf.coef_.shape[0]):
            word_importances = [(el, index_to_word[i]) for i,el in enumerate(clf_tfidf.coef_[class_index])]
            sorted_coeff = sorted(word_importances, key = lambda x : x[0], reverse=True)
            tops = sorted(sorted_coeff[:n], key = lambda x : x[0])
            bottom = sorted_coeff[-n:]
            classes[class_index] = {
                'tops':tops,
                'bottom':bottom
            }
        return classes
    
    def plot_important_words(self, X_train, y_train, vectoriser, name):
        #To see the most relevant word for class 1
        importance = self.get_most_important_features(X_train, y_train, vectoriser, 10)
        top_scores = [a[0] for a in importance[1]['tops']]
        top_words = [a[1] for a in importance[1]['tops']]
        bottom_scores = [a[0] for a in importance[1]['bottom']]
        bottom_words = [a[1] for a in importance[1]['bottom']]
    
        y_pos = np.arange(len(top_words))
        top_pairs = [(a,b) for a,b in zip(top_words, top_scores)]
        top_pairs = sorted(top_pairs, key=lambda x: x[1])
    
        bottom_pairs = [(a,b) for a,b in zip(bottom_words, bottom_scores)]
        bottom_pairs = sorted(bottom_pairs, key=lambda x: x[1], reverse=True)
    
        top_words = [a[0] for a in top_pairs]
        top_scores = [a[1] for a in top_pairs]
    
        bottom_words = [a[0] for a in bottom_pairs]
        bottom_scores = [a[1] for a in bottom_pairs]
    
        fig = plt.figure(figsize=(10, 10))  

        plt.subplot(121)
        plt.barh(y_pos,bottom_scores, align='center', alpha=0.5)
        plt.title('Non-closure', fontsize=20)
        plt.yticks(y_pos, bottom_words, fontsize=14)
        plt.suptitle('Key words', fontsize=16)
        plt.xlabel('Importance', fontsize=20)
    
        plt.subplot(122)
        plt.barh(y_pos,top_scores, align='center', alpha=0.5)
        plt.title('Closure', fontsize=20)
        plt.yticks(y_pos, top_words, fontsize=14)
        plt.suptitle(name, fontsize=16)
        plt.xlabel('Importance', fontsize=20)
    
        plt.subplots_adjust(wspace=0.8)
        plt.show()
        return None