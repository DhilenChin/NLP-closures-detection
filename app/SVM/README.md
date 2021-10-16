# Using SVM to classify tweets
Support Vector Machine can be used to classify tweets into closure/non-closure related.
## Training steps
1. Save a list of tweets in the below format in a `.csv` file.<br> Class 0 - Non-closure<br> Class 1 -Closure-related<br> Class 2- Unsure

| Content                         | class_label  | 
| -------------                   |:-------------:| 
| Closure at M60 between J2 and J3.| 1 | 
|Everyone needs a closure.        | 0 |   
| Theres is currently a closure here.| 2 |

2. In a python file, run the following to train the model and see the prediction.
```python
from SVM.SVM_model import SVM_model
svm = SVM_model(df = pd.read_csv("./directory/to/your/data.csv"))
svm.training()
svm.predict('Your text here to be predicted')
```
3. `metrics_tools` provide a list of metrics to check and test the accuracy/precision of your SVM model.
