# -*- coding: utf-8 -*-
"""mobile_price_range_classification.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tYIzendTZauKei2cfcFt0Uqm8frWY-bS

The problem statement given below:

Bob has started his own mobile company. He wants to give tough fight to big companies like Apple,Samsung etc.

He does not know how to estimate price of mobiles his company creates. In this competitive mobile phone market you cannot simply assume things. To solve this problem he collects sales data of mobile phones of various companies.

Bob wants to find out some relation between features of a mobile phone(eg:- RAM,Internal Memory etc) and its selling price. But he is not so good at Machine Learning. So he needs your help to solve this problem.

In this problem you do not have to predict actual price but a price range indicating how high the price is.



---
So for this problem statement we will proceed with following steps to classify the target variable i.e. price_range with value of 0(low cost), 1(medium cost), 2(high cost) and 3(very high cost):

- Data training using the mobile price classification dataset. 
- Model creation which will include importing logistic regression from sklearn, initializing the classifier, then fit the training data into it and perform classification.
---

For the dataset being used [click here](https://www.kaggle.com/iabhishekofficial/mobile-price-classification?select=train.csv)

#### Data Preprocessing and Exploration.
"""

# importing pandas library.
import pandas as pd

data = pd.read_csv("/content/train.csv")
data

# converting data into int datatype to avoid errors below.
prepareddata = data.astype(int)
prepareddata.head()

"""#### Data Training & Model Creation.

Data Training:
"""

# Import train_test_split from sklearn.model_selection
from sklearn.model_selection import train_test_split

# Here, x is the data which will have features for classification and y will have our target i.e. price range of the mobiles.
x = prepareddata.drop(["price_range"], axis=1)
y = prepareddata["price_range"]

# Split data into training data and testing data.
# Ratio used for splitting training and testing data is 8:2 respectively
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=100
)

"""Model Creation:"""

# Importing logistic regression model
from sklearn.linear_model import LogisticRegression

clfr = LogisticRegression()

# Fitting data into the model.
clfr.fit(x_train, y_train)

# Making predictions
pred = clfr.predict(x_test)

pred

"""The above predictions are made by Logistic Regression model."""
