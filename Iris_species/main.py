import pandas as pd 
import numpy as np 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 

iris = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)


# initializing the model 
knc = KNeighborsClassifier(n_neighbors=1) 
# training the model
knc.fit(x_train, y_train) 
# predicting the y
y_pred = knc.predict(x_test) 

# finding the accuracy using numpy mean 
print("test set score: {:.2f}".format(np.mean(y_pred == y_test)))
# finding the accuracy using inbuild method
print("test set score: {:.2f}".format(knc.score(x_test, y_test)))