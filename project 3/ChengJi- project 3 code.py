# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 22:42:52 2016

@author: guaisang
"""

# import data and check everything
import pandas as pd
df = pd.read_csv('~/desktop/CreditDefault.csv', index_col='ID')
df.head()
df.dtypes
df.shape
df.isnull().sum()

# rename column for easy reference
df.rename(columns={'default payment next month': 'default'}, inplace=True)
df.columns=df.columns.str.lower()

# check the benchmark
df.default.value_counts()

# by looking at the column names, there might be multicollinearity issues here,
# so check the correlation matrix to confirm
df.corr()

# plot columns with similar names to check the correlation
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
sns.pairplot(df, vars=df.columns[11:17], kind='scatter')
sns.pairplot(df, vars=df.columns[17:23])

# manually standardize numeric columns
col_to_norm = ['limit_bal', 'age', 'bill_amt1', 'bill_amt2', 'bill_amt3', 'bill_amt4', 'bill_amt5', 'bill_amt6',
              'pay_amt1', 'pay_amt2', 'pay_amt3', 'pay_amt4', 'pay_amt5', 'pay_amt6']

import numpy as np
df[col_to_norm]=df[col_to_norm].apply(lambda x: (x-np.mean(x))/np.std(x))

# create dummies for categorical features.
# add 2 to all the values because OneHotEncoder can only handle non-negative values
col_pay = ['pay_0', 'pay_2', 'pay_3', 'pay_4', 'pay_5', 'pay_6']
df[col_pay] = df[col_pay].apply(lambda x: x+2)

from sklearn.preprocessing import OneHotEncoder
X = df.iloc[:, 0:23]
y = df.default
enc = OneHotEncoder(categorical_features=[1,2,3,5,6,7,8,9,10])
X = enc.fit_transform(X)

from sklearn.cross_validation import train_test_split, cross_val_score
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=df.default, random_state=1)

from sklearn.linear_model import LogisticRegressionCV, SGDClassifier
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import roc_curve, auc, classification_report
from sklearn.feature_selection import RFECV

# try using stochastic gradient descent with logistic loss function
# specify lasso regularization to select features and address multicollinearity issues
sgd = SGDClassifier(loss='log', penalty='l1', learning_rate='optimal')
# use grid search to optimize parameters
search_params = {'alpha': [0.0001, 0.001, 0.01, 0.1, 1.0, 5.0], 'class_weight': [None, 'balanced']}
estimator  = GridSearchCV(sgd, search_params)
model = estimator.fit(X_train, y_train)

print 'Best Params: ', model.best_params_
print 'Best Score: ', model.best_score_
y_pred = model.predict(X_test)

# create classification report
print classification_report(y_test, y_pred, target_names=['not default', 'default'])

# create confusion matrix
from sklearn.metrics import confusion_matrix
conmat = np.array(confusion_matrix(y_test, y_pred, labels=[1,0]))
confusion = pd.DataFrame(conmat, index=['default', 'not default'], columns=['predicted default', 'predicted not default'])
print confusion

# plot roc curve and calculate auc
y_score = model.decision_function(X_test)
fpr = dict()
tpr = dict()
roc_auc=dict()
fpr[1], tpr[1], _ = roc_curve(y_test, y_score)
roc_auc[1] = auc(fpr[1], tpr[1])

plt.figure(figsize=[9,7])
plt.plot(fpr[1], tpr[1], label='Roc curve (area=%0.2f)' %roc_auc[1], linewidth=4)
plt.plot([1,0], [1,0], 'k--', linewidth=4)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('false positive rate', fontsize=18)
plt.ylabel('true positive rate', fontsize=18)
plt.title('ROC curve for credit default', fontsize=18)
plt.legend(loc='lower right')
plt.show()

# logistic regression with grid search
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(solver='liblinear')
search_params = {'C': [0.001, 0.01, 0.1, 1, 10], 'class_weight': [None, 'balanced'], 'penalty': ['l1', 'l2']}
estimator = GridSearchCV(lr, search_params)
estimator.fit(X_train, y_train)
print "Best Params:", estimator.best_params_
print "Best Score:", estimator.best_score_

# feature selection with the best model from grid search
lr = LogisticRegression(penalty='l1', C=1, solver='liblinear')
rfecv = RFECV(estimator=lr, scoring='accuracy')
model = rfecv.fit(X, y)
pred_y = model.predict(X_test)

# print evaluation matrices
print classification_report(y_test, pred_y, target_names=['not default', 'default'])

conmat = np.array(confusion_matrix(y_test, pred_y, labels=[1,0]))
confusion = pd.DataFrame(conmat, index=['default', 'not default'], columns=['predicted default', 'predicted not default'])
print confusion

y_score = model.decision_function(X_test)
fpr = dict()
tpr = dict()
roc_auc=dict()
fpr[1], tpr[1], _ = roc_curve(y_test, y_score)
roc_auc[1] = auc(fpr[1], tpr[1])

plt.figure(figsize=[9,7])
plt.plot(fpr[1], tpr[1], label='Roc curve (area=%0.2f)' %roc_auc[1], linewidth=4)
plt.plot([1,0], [1,0], 'k--', linewidth=4)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('false positive rate', fontsize=18)
plt.ylabel('true positive rate', fontsize=18)
plt.title('ROC curve for credit default', fontsize=18)
plt.legend(loc='lower right')
plt.show()

# curious about how k nearest neighbors perform with binary problem
from sklearn.neighbors import KNeighborsClassifier
search_parameters = {'n_neighbors': [1, 3, 5, 10, 50], 'weights': ('uniform', 'distance'),
                     'algorithm': ('brute', 'auto'), 'p': [1,2]}
knn = KNeighborsClassifier()
clf = GridSearchCV(knn, search_parameters)
clf.fit(X_train, y_train)
print 'Best Parameters:', clf.best_params_
print 'Best Score:', clf.best_score_

knnpred_y = clf.predict(X_test)
print classification_report(y_test, knnpred_y, target_names=['not default', 'default'])

conmat = np.array(confusion_matrix(y_test, knnpred_y, labels=[1,0]))
confusion = pd.DataFrame(conmat, index=['default', 'not default'], columns=['predicted default', 'predicted not default'])
print confusion
