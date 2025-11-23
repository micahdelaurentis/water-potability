import pandas as pd 
import numpy as np
import pickle 
import os 
from sklearn.ensemble import RandomForestClassifier
import yaml 

n_estimators = yaml.safe_load(open('params.yaml'))['model_building']['n_estimators']


train_data = pd.read_csv('./data/processed/train_processed.csv')

X_train = train_data.drop(columns = ['Potability'], axis = 1)
y_train = train_data['Potability']

clf = RandomForestClassifier(n_estimators= n_estimators)

clf.fit(X_train, y_train)

pickle.dump(clf, open('model.pkl','wb'))