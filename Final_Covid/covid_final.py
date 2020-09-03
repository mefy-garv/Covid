# -*- coding: utf-8 -*-
"""Covid_Final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gomQsYs1tFB2q6ZT9hQ77ERlIimuImuv
"""

# import libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'covid.csv')

df.head()

# df = df.sample(frac=1)

# df.head()

# df.to_csv('newfile.csv')

df.isnull().sum()

df.dtypes



df['Linfociti'] = pd.to_numeric(df['Linfociti'], errors='coerce')

df.dtypes





sns.heatmap(df.isnull(),yticklabels=False,cbar=False)

df.shape

df['WBC']=df['WBC'].fillna(df['WBC'].mean())

df['Piastrine']=df['Piastrine'].fillna(df['Piastrine'].mean())

df['Neutrofili']=df['Neutrofili'].fillna(df['Neutrofili'].mean())

df['Linfociti']=df['Linfociti'].fillna(df['Linfociti'].mean())

#df["Linfociti"]= df['Linfociti'].fillna(df['Linfociti'].mode()[0])



df['Monociti']=df['Monociti'].fillna(df['Monociti'].mean())

# df["Eosinofili"]= df['Eosinofili'].fillna(df['Eosinofili'].mode()[0])

df["Basofili"]= df['Basofili'].fillna(df['Basofili'].mode()[0])

df['Eosinofili']=df['Eosinofili'].fillna(df['Eosinofili'].mean())

# df['Basofili']=df['Basofili'].fillna(df['Basofili'].mean())

df['PCR']=df['PCR'].fillna(df['PCR'].mean())

df['AST']=df['AST'].fillna(df['AST'].mean())

df['ALT']=df['ALT'].fillna(df['ALT'].mean())

df['ALP']=df['ALP'].fillna(df['ALP'].mean())

df['GGT']=df['GGT'].fillna(df['GGT'].mean())

df['LDH']=df['LDH'].fillna(df['LDH'].mean())

df.isnull().sum()

df['SESSO'].value_counts()

drop_columns = ["PCR"]
df.drop(labels= drop_columns, axis=1, inplace=True)

# drop_columns = ["GGT"]
# df.drop(labels= drop_columns, axis=1, inplace=True)

# drop_columns = ["SESSO"]
# df.drop(labels= drop_columns, axis=1, inplace=True)

drop_columns = ["Linfociti"]
df.drop(labels= drop_columns, axis=1, inplace=True)

df.shape

# Lets convert male to 0 and female to 1:
df['SESSO'].replace(to_replace=['M','F'], value=[0,1],inplace=True)
df.head()

x = df.iloc[:, :-1].values
y = df.iloc[:, 13].values

"""**K Nearest Neighbor(KNN)**"""

# Train Test Split

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

# Preprocessing

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x_train)

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred))

error = []

# Calculating error for K values between 1 and 40
for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(x_train, y_train)
    pred_i = knn.predict(x_test)
    error.append(np.mean(pred_i != y_test))

plt.figure(figsize=(12, 6))
plt.plot(range(1, 40), error, color='red', linestyle='dashed', marker='o',
         markerfacecolor='blue', markersize=10)
plt.title('Error Rate K Value')
plt.xlabel('K Value')
plt.ylabel('Mean Error')

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 24)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred))



"""**Decision Tree**"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10)

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion="entropy", max_depth = 2)
classifier # it shows the default parameters

classifier.fit(x_train,y_train)

y_pred = classifier.predict(x_test)

from sklearn import metrics
import matplotlib.pyplot as plt
print("DecisionTrees's Accuracy: ", metrics.accuracy_score(y_test, y_pred))



"""**Support Vector Machine**"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20,random_state = 10)

# Polynomial Kernel
from sklearn.svm import SVC   # Support Vector Classifier
classifier = SVC(kernel ='rbf')
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

# Evaluating the Algorithm
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred))



"""**XGBoost**"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20,random_state = 10)

from sklearn.preprocessing import MinMaxScaler

#Feature Scaling
# We'll now scale our data by creating an instance of the scaler and scaling it:

scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

import xgboost
classifier=xgboost.XGBClassifier()

booster=['gbtree','gblinear']
base_score=[0.25,0.5,0.75,1]

## Hyper Parameter Optimization


n_estimators = [100, 500, 900, 1100, 1500]
max_depth = [2, 3, 5, 10, 15]
booster=['gbtree','gblinear']
learning_rate=[0.05,0.1,0.15,0.20]
min_child_weight=[1,2,3,4]

# Define the grid of hyperparameters to search
hyperparameter_grid = {
    'n_estimators': n_estimators,
    'max_depth':max_depth,
    'learning_rate':learning_rate,
    'min_child_weight':min_child_weight,
    'booster':booster,
    'base_score':base_score
    }

from sklearn.model_selection import RandomizedSearchCV

# Set up the random search with 4-fold cross validation
random_cv = RandomizedSearchCV(estimator=classifier,
            param_distributions=hyperparameter_grid,
            cv=5, n_iter=50,
            scoring = 'neg_mean_absolute_error',n_jobs = -1,
            verbose = 5, 
            return_train_score = True,
            random_state=42)

random_cv.fit(x_train,y_train)

random_cv.best_estimator_

random_cv.best_estimator_

classifier=xgboost.XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
              colsample_bynode=1, colsample_bytree=1, gamma=0,
              learning_rate=0.1, max_delta_step=0, max_depth=2,
              min_child_weight=1, missing=None, n_estimators=100, n_jobs=1,
              nthread=None, objective='binary:logistic', random_state=0,
              reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,
              silent=None, subsample=1, verbosity=1)

classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

y_pred

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred))

# Evaluating the Algorithm

# Let's find the values for these metrics using our test data. Execute the following code:

from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))





from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20,random_state = 10)

import xgboost
classifier=xgboost.XGBClassifier()
classifier.fit(x_train,y_train)

y_pred = classifier.predict(x_test)

y_pred

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred))





import re

pip install catboost

from catboost import CatBoostClassifier

import lightgbm as lgb

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20,random_state = 10)

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import BaggingClassifier,AdaBoostClassifier,ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier

#classifier=ExtraTreesClassifier()
#classifier = GradientBoostingClassifier()
#classifier=AdaBoostClassifier()
#classifier=RandomForestClassifier()
classifier=GradientBoostingClassifier()
#classifier=lgb.LGBMClassifier()
#classifier = BaggingClassifier()
#classifier = CatBoostClassifier()
#classifier.fit(X_train,y_train)

classifier = GradientBoostingClassifier()
classifier.fit(x_train, y_train)

#import xgboost
#classifier=xgboost.XGBRFClassifier()
#classifier.fit(X_train,y_train)

y_pred = classifier.predict(x_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred))





"""**Logistic Regression**"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split( x, y, test_size=0.2, random_state=10)

from sklearn.linear_model import LogisticRegression
LR = LogisticRegression(C=0.01, solver='liblinear')
LR.fit(x_train,y_train)

LR_pred = LR.predict(x_test)

## Evaluating the Algorithm
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test, LR_pred))
print(classification_report(y_test, LR_pred))
print(accuracy_score(y_test, LR_pred))





"""**Random Forest**"""

# Now that we have our attributes and labels, the next step is to split this data into training and test sets. 
# We'll do this by using Scikit-Learn's built-in train_test_split() method:

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Train the Algorithm
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 200, random_state=0)
classifier.fit(x_train, y_train)

import pickle
filename = 'classifier.pkl'
pickle.dump(classifier, open(filename, 'wb'))

y_pred = classifier.predict(x_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred))



"""**Naive Bayes**"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# import Gaussian Naive Bayes import GaussianNB
from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier 
gnb = GaussianNB()

# Train the model using the training sets
gnb.fit(x_train, y_train)

# Predict the response for the test dataset
y_pred = gnb.predict(x_test)

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))













dataset['Gender'] = dataset['Gender'].astype('float')
dataset.head()

import pickle
filename = 'finalized_model.pkl'
pickle.dump(classifier, open(filename, 'wb'))

# Evaluating the Algorithm

# Let's find the values for these metrics using our test data. Execute the following code:

from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

y_pred.shape

##Create Sample Submission file and Submit using ANN
pred=pd.DataFrame(y_pred)
sub_df=pd.read_csv('sample_submission.csv')
datasets=pd.concat([sub_df['Id'],pred],axis=1)
datasets.columns=['Id','Age']
datasets.to_csv('sample_submission.csv',index=False)