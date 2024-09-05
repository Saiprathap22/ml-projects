# -*- coding: utf-8 -*-
"""IMPACT OF YOUTUBE ADVERTISEMENTS ON SALES.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10-uTYaKdn6o-pHsDDuN4CzodVknlBZ0E
"""

# Supress Warnings

import warnings
warnings.filterwarnings('ignore')

# Import the numpy and pandas package

import numpy as np
import pandas as pd

# Data Visualisation
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded = files.upload()

advertising = pd.DataFrame(pd.read_csv(r"advertising.csv"))
advertising.head()

"""Data Inspection"""

advertising.shape

advertising.info()

advertising.describe()

"""Data Cleaning"""

# Checking Null values
advertising.isnull().sum()*100/advertising.shape[0]
# There are no NULL values in the dataset, hence it is clean.

# Outlier Analysis
fig, axs = plt.subplots(3, figsize = (5,5))
plt1 = sns.boxplot(advertising['youtube'], ax = axs[0])
plt2 = sns.boxplot(advertising['youtubemusic'], ax = axs[1])
plt3 = sns.boxplot(advertising['youtubekids'], ax = axs[2])
plt.tight_layout()

sns.boxplot(advertising['Sales'])
plt.show()

# Let's see how Sales are related with other variables using scatter plot.
sns.pairplot(advertising, x_vars=['youtube', 'youtubemusic', 'youtubekids'], y_vars='Sales', height=4, aspect=1, kind='scatter')
plt.show()

# Let's see the correlation between different variables.
sns.heatmap(advertising.corr(), cmap="YlGnBu", annot = True)
plt.show()

X = advertising['youtube']
y = advertising['Sales']

"""Train-Test Split"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, test_size = 0.3, random_state = 100)
# Let's now take a look at the train dataset

X_train.head()

y_train.head()

"""Building a Linear Model"""

import statsmodels.api as sm

# Add a constant to get an intercept
X_train_sm = sm.add_constant(X_train)

# Fit the resgression line using 'OLS'
lr = sm.OLS(y_train, X_train_sm).fit()
# Print the parameters, i.e. the intercept and the slope of the regression line fitted
lr.params

# Performing a summary operation lists out all the different parameters of the regression line fitted
print(lr.summary())

plt.scatter(X_train, y_train)
plt.plot(X_train, 6.948 + 0.054*X_train, 'r')
plt.show()

"""Model Evaluation

Distribution of the error terms
"""

y_train_pred = lr.predict(X_train_sm)
res = (y_train - y_train_pred)
fig = plt.figure()
sns.distplot(res, bins = 15)
fig.suptitle('Error Terms', fontsize = 15)
 # Plot heading
plt.xlabel('y_train - y_train_pred', fontsize = 15)
 # X-label
plt.show()

"""Looking for patterns in the residuals"""

plt.scatter(X_train,res)
plt.show()

"""Predictions on the Test Set"""

# Add a constant to X_test
X_test_sm = sm.add_constant(X_test)

# Predict the y values corresponding to X_test_sm
y_pred = lr.predict(X_test_sm)
y_pred.head()



import numpy as np
import matplotlib.pyplot as plt

def coeff(x,y):
    mx=np.mean(x)
    my=np.mean(y)
    b1=sum((x-mx)*(y-my))/sum((x-mx)**2)
    b0=my-b1*mx
    return(b1,b0)

#def plotgra(x,y,b):
    #plt.scatter(x,y,c='blue', marker='*')
    #plt.xlabel('study hour')
    #plt.ylabel('grade')
    #yp=b[0]+b[1]*x
    #plt.plot(x,yp)
    #plt.show()


def main():
    x=np.array([1,2,3,4,5])
    y=np.array([2,4,5,4,5])
    b=coeff(x,y)
    print(b[0])
    print(b[1])
    plotgra(x,y,b)

if __name__ == "__main__" :
     main()

"""Looking at the RMSE"""

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
#Returns the mean squared error; we'll take a square root
np.sqrt(mean_squared_error(y_test, y_pred))

"""Checking the R-squared on the test set"""

r_squared = r2_score(y_test, y_pred)
r_squared

"""Visualizing the fit on the test set"""

plt.scatter(X_test, y_test)
plt.plot(X_test, 6.948 + 0.054 * X_test, 'r')
plt.show()