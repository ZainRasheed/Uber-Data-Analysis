# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 09:30:12 2019

@author: MohammedS2
"""

#Import tha libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Importing the data
Uber = pd.read_csv("C:/Users/mohammeds2/OneDrive - Verifone/Desktop/New folder (4) ML/Uber data/Uber_Request_Data.csv")

#Checking for duplicate rows
#if te max od count is 1, no duplicate
#if the grapg is not being plotted, duplicate exist
X = Uber["Request id"]
X_Count = X.value_counts()
X_Count_max = X_Count.max()
plt.plot(X,X_Count)

#remove the col
Uber = Uber.iloc[:,1:6]

# replacing th nan values with 0
X = Uber["Driver id"].copy()
X_bool = pd.isnull(X)
X[X_bool] = 0
Uber["Driver id"] = X

'''USING COPY TO AVOID WARNING'''
'''__main__:3: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame'''

X = Uber["Drop timestamp"].copy()
X_bool = pd.isnull(X)
X[X_bool] = 0
Uber["Drop timestamp"] = X

#Removing month, day, year from the time stamps and getting a single format
#month and day are same
#days is linear
X = Uber["Drop timestamp"]
X = pd.to_datetime(X) #converting to numoy datetime type dtype('<M8[ns]')
X = X.dt.strftime('%S:%M:%H')
Uber["Drop timestamp"] = X

X = Uber["Request timestamp"]
X = pd.to_datetime(X) #converting to numoy datetime type dtype('<M8[ns]')
X = X.dt.strftime('%S:%M:%H')
Uber["Request timestamp"] = X

"""Uni analysis"""
Uber.describe()
Uber["Pickup point"].value_counts()
Uber["Driver id"].value_counts()
Uber["Status"].value_counts()
Uber["Request timestamp"].value_counts()
Uber["Drop timestamp"].value_counts()

Uber["Pickup point"].hist()
plt.plot()
plt.show()
Uber["Driver id"].hist()
Uber["Status"].hist()
Uber["Request timestamp"].hist()
Uber["Drop timestamp"].hist()
plt.plot()