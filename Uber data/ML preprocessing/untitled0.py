# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 19:03:03 2019

@author: MohammedS2
"""

#importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

#Creating dataset location vairable
file_location = "C:\\Users\\mohammeds2\\OneDrive - Verifone\\Desktop\\New folder (4) ML\\Uber data\\Uber_Request_Data.csv"

#Reading the file
Uber = pd.read_csv(file_location)

#Fetching the Request id column   
#X = Uber.iloc[:,0].values
#Looking for the duplicate number in Request id by counting the reptations for each cell in request id 
#Checking the maxinum number from the X_Count list, if the maximum is 1 then there is no repeated number
X = Uber["Request id"]
X_Count = X.value_counts()
X_COUNT_Max = X_Count.max()
plt.plot(X,X_Count)
Uber = Uber.iloc[:,1:6]

#Fetching the Pickup point column   
#Looking for the duplicate number in Pickup point by counting the reptations for each cell in request id 
X = Uber["Pickup point"]
X_Count = X.value_counts()

#Fillinh nan with a int
#X = Uber[["Driver id","Drop timestamp"]]
X = Uber["Driver id"]
X_bool = X.isnull()
Uber.loc[X_bool,"Driver id"] = 0

X = Uber["Drop timestamp"]
X_bool = X.isnull()
Uber.loc[X_bool,"Drop timestamp"] = 0
#Y = Uber.iloc[:,5]

X = Uber["Status"]
X_Count = X.value_counts()
X.describe()

#Converting all the time date to same format
#removing year, day, date
X = Uber["Request timestamp"]
X_Count = X.value_counts()
X = pd.to_datetime(X) #converting string to date type
#Uber['Request timestamp'] = X.dt.strftime('%m/%d/%y %H:%M:%S')
Uber['Request timestamp'] = X.dt.strftime('%H:%M:%S')

X = Uber["Drop timestamp"]
X_Count = X.value_counts()
X = pd.to_datetime(X) #converting string to date type
Uber['Drop timestamp'] = X.dt.strftime('%H:%M:%S')

""" UNI analysis """

Uber.shape

Uber.describe()

Uber["Pickup point"].describe()
Uber["Driver id"].describe()
Uber["Status"].describe()
Uber["Request timestamp"].describe()
Uber["Drop timestamp"].describe()

Uber["Pickup point"].value_counts()
Uber["Driver id"].value_counts()
Uber["Status"].value_counts()
Uber["Request timestamp"].value_counts()
Uber["Drop timestamp"].value_counts()