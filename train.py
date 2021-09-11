import os
import json
from time import time
import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import svm
import pickle

# Set filepath
ROOT = os.path.abspath(".")
filepath = os.path.join(ROOT, "data/Iris.csv")

# Read data
iris = pd.read_csv(filepath) 
print(iris.head())

# Remove id columns
iris.drop('Id',axis=1,inplace=True)


# Model
train, test = train_test_split(iris, test_size = 0.3)


train_X = train[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]# taking the training data features
train_y = train.Species# output of our training data
test_X = test[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']] # taking test data features
test_y = test.Species

# Fit model
model = svm.SVC()
model.fit(train_X,train_y)
begin_time = time()
prediction=model.predict(test_X) 
elasped_time = (time() - begin_time)/1000

accuracy = metrics.accuracy_score(prediction,test_y)

print('The accuracy of SVM model is:', accuracy)
print('The elasped Time is :', str(round(elasped_time)), " seconds")

if not os.path.exists("model") : 
    os.mkdir("model")

with open("model/model.pkl", mode="wb") as m : 
    pickle.dump(model, m)
print("model dumped !!!")

log = {"prediction" : accuracy, "elasped_time" : elasped_time}
print(log)

# Log for test
with open("./log.json", mode  = "w", encoding="utf8") as f : 
    json.dump(log, f)


print(model.predict(np.array([1 , 4, 3 , 4]).reshape(1,-1)))
