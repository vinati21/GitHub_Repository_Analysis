
# data base
import pymysql
from sqlalchemy import create_engine
import MySQLdb

#importing pickle
import pickle

import numpy as np
import pandas as pd
import math
from matplotlib import pyplot as plt
import seaborn as sns

#Importing bokeh

from bokeh.plotting import figure
from bokeh.io import show, output_notebook
from bokeh.models import HoverTool
from bokeh.palettes import Spectral6
from bokeh.models import ColumnDataSource

#Feature selection
from sklearn.feature_selection import chi2

# for splitting the data set
from sklearn.model_selection import train_test_split


#tf-idf libraries 
from sklearn.feature_extraction.text import TfidfVectorizer

#importing truncated svd for LSA- Latent Semantic Analysis
from sklearn.decomposition import TruncatedSVD

#Importing tsne
from sklearn.manifold import TSNE

#Label Encoding
# import labelencoder
from sklearn.preprocessing import LabelEncoder

np.random.seed(100)

# Importing Decision Tree
from sklearn.ensemble import RandomForestClassifier


#For tuning the hyper-parameters

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV

#importing metrics

from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

# UnPickling all the files so that I can use it for modeling


# X_train
with open('/home/isiia/Github_Classification/Pickles/X_train.pickle', 'rb') as data:
    X_train= pickle.load(data)
    
# X_test    
with open('/home/isiia/Github_Classification/Pickles/X_test.pickle', 'rb') as data:
    X_test=pickle.load(data)
    
# y_train
with open('/home/isiia/Github_Classification/Pickles/Y_train.pickle', 'rb') as data:
    Y_train=pickle.load(data)
    
# y_test
with open('/home/isiia/Github_Classification/Pickles/Y_test.pickle', 'rb') as data:
    Y_test=pickle.load(data)
    
# df
with open('/home/isiia/Github_Classification/Pickles/df_repo.pickle', 'rb') as data:
    df_repo=pickle.load(data)
    
# Tf-idf vectorized train dataset
with open('/home/isiia/Github_Classification/Pickles/vz_train.pickle', 'rb') as data:
    vz_train=pickle.load(data)

# Tf-idf vectorized test dataset
with open('/home/isiia/Github_Classification/Pickles/vz_test.pickle', 'rb') as data:
    vz_test=pickle.load(data)

# Class dictionary
with open('/home/isiia/Github_Classification/Pickles/class_dict.pickle', 'rb') as data:
    class_dict=pickle.load(data)

#tfidf data frame for train
with open('/home/isiia/Github_Classification/Pickles/tfidf_df.pickle', 'rb') as data:
    tfidf_df=pickle.load(data)
    
# #svd data train
# with open('/home/isiia/Github_Classification/Pickles/svd_train.pickle', 'rb') as data:
#     svd_train=pickle.load(data)

# #svd data test
# with open('/home/isiia/Github_Classification/Pickles/svd_test.pickle', 'rb') as data:
#     svd_test=pickle.load(data)
    
# #svd data train dataframe
# with open('/home/isiia/Github_Classification/Pickles/df_svd_train.pickle', 'rb') as data:
#     df_svd_train=pickle.load(data)

# #svd data test dataframe
# with open('/home/isiia/Github_Classification/Pickles/df_svd_test.pickle', 'rb') as data:
#     df_svd_test=pickle.load(data)

base_model=RandomForestClassifier()
# svd_train

# import time
# t0=time.time()
# base_model.fit(svd_train,Y_train.values)
# t1=time.time()-t0
# print("Time Taken for base model is",t1)

# print("The training score is ")
# print(base_model.score(svd_train,Y_train.values)*100)

# print("The test score is")
# base_model.score(svd_test,Y_test.values)*100

base_model_new=RandomForestClassifier(n_estimators=200,max_depth=350,n_jobs=-1,min_samples_leaf=4,min_samples_split=4,warm_start=True,verbose=1)
import time
t0=time.time()
base_model_new.fit(vz_train.toarray(),Y_train.values)
t1=time.time()-t0
print(t1)

print("The training score is ")
print(base_model_new.score(vz_train.toarray(),Y_train.values)*100)

print("The test score is")
base_model_new.score(vz_test.toarray(),Y_test.values)*100

## If we see the above results implies that the model is overfitting.

## Lets Tune the RandomForest

base_model.get_params

## Using RandomizedGridSearchCV

# I will be selecting criterion, max_depth, max_features,min_samples_leaf,min_samples_split,bootstrap,n_estimators
# defining a range for all of these

n_estimators = [200]
bootstrap=['False']
criterion=['gini']
# max_depth
max_depth = [350]
#max_depth.append(None)

max_features=['log2']
min_samples_leaf=[2,4,6,8,10]
min_samples_split=[2,5,10]

random_grid={'n_estimators':n_estimators,'bootstrap':bootstrap,'criterion':criterion, 'max_depth':max_depth, 'max_features':max_features,'min_samples_leaf':min_samples_leaf,'min_samples_split':min_samples_split}
print(random_grid)

random_search=RandomizedSearchCV(estimator=base_model,param_distributions=random_grid,scoring='accuracy',cv=5,return_train_score=True,n_jobs=-1)

t0=time.time()
random_search.fit(vz_train.toarray(),Y_train.values)
t1=time.time()-t0
print("Time taken for Random Search CV is ",t1)
print("The best params are:",random_search.best_params_)
print("The best estimator is :",random_search.best_estimator_)
print("The best score is :",random_search.best_score_)

# Training accuracy
print("The training accuracy is: ")
train_acc=accuracy_score(Y_train, random_search.predict(vz_train.toarray()))*100
print(train_acc)

#Test Accuracy
print("The test accuracy is: ")
test_acc=accuracy_score(Y_test, random_search.predict(vz_test.toarray()))*100
print(test_acc)
