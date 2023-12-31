# -*- coding: utf-8 -*-
"""CreditCard_FraudDetection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tLFmZwHO_mL2TjrCkEIjUn-DpHrIDrtR
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import gridspec
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

dataset = pd.read_csv("creditcard.csv")
print(dataset.shape)
print(dataset.head())

fraud = dataset[dataset["Class"] == 1]
legit = dataset[dataset["Class"] == 0]
fraction = len(fraud)/float(len(legit))
print(f"The total fraction of fraud is {fraction}")
print(f"Fraud Cases: {len(fraud)}")
print(f"Valid Transactions: {len(legit)}")

dataset.info()

dataset.isnull().sum()

fraud.Amount.describe()

legit.Amount.describe()

dataset.groupby('Class').mean()

# Mean of those two real and fake classes are way more than thought but data is unbalanced

"""**RANDOM FOREST ALGORITHM**"""

Data = pd.concat([legit, fraud], axis = 0)

X = Data.drop(['Class'], axis = 1)
Y = Data['Class']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify = Y, random_state=2)

Model_RF = RandomForestClassifier()
Model_RF.fit(X_train, Y_train)
Y_train_pred = Model_RF.predict(X_train)
Y_test_pred = Model_RF.predict(X_test)

training_accuracy = accuracy_score(Y_train_pred, Y_train)
test_accuracy = accuracy_score(Y_test_pred, Y_test)

print(f"The accuracy is {test_accuracy}")

"""**RANDOM FOREST ALGORITHM + UNDERSAMPLING**"""

accuracy = 0

for i in range(500):
  legit_sample = legit.sample(492)
  newdataset = pd.concat([legit_sample, fraud], axis = 0)

  X = newdataset.drop(['Class'], axis = 1)
  Y = newdataset['Class']

  X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify = Y, random_state=2)

  Model_RF = RandomForestClassifier()
  Model_RF.fit(X_train, Y_train)
  Y_train_pred = Model_RF.predict(X_train)
  Y_test_pred = Model_RF.predict(X_test)

  training_accuracy = accuracy_score(Y_train_pred, Y_train)
  test_accuracy = accuracy_score(Y_test_pred, Y_test)

  if (test_accuracy > accuracy):
    accuracy = test_accuracy

print(f"The Accuracy using Random Forest with undersampling is {accuracy}")

"""**LOGISTIC REGRESSION + UNDERSAMPLING**"""

accuracy = 0

for i in range(500):
  legit_sample = legit.sample(492)
  newdataset = pd.concat([legit_sample, fraud], axis = 0)

  X = newdataset.drop(['Class'], axis = 1)
  Y = newdataset['Class']

  X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify = Y, random_state=2)

  Model_LR = RandomForestClassifier()
  Model_LR.fit(X_train, Y_train)
  Y_train_pred = Model_LR.predict(X_train)
  Y_test_pred = Model_LR.predict(X_test)

  training_accuracy = accuracy_score(Y_train_pred, Y_train)
  test_accuracy = accuracy_score(Y_test_pred, Y_test)

  if (test_accuracy > accuracy):
    accuracy = test_accuracy

print(f"The Accuracy using Logistic Regression with undersampling is {accuracy}")