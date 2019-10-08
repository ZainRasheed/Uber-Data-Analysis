# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 09:30:12 2019

@author: MohammedS2
"""

#Import tha libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


#Importing the data
Uber = pd.read_csv("C:/Users/mohammeds2/OneDrive - Verifone/Desktop/New folder (4) ML/Uber data/Uber_Request_Data.csv")
#Data imported into a dataframe 'Uber'



#Checking for duplicate rows in RequestID
#And removing if no duplicates
''' FAILED or bad strategy
X = Uber["Request id"]
X_Count = X.value_counts()
X_Count_max = X_Count.max()   #if te max od count is 1, no duplicate
plt.plot(X,X_Count)     #if the grapg is not being plotted, duplicate exist 
'''
X = Uber["Request id"]
#Copied the column into 'X'

'''X_Count = X.repeat(repeats > n) // doesn't work '''
'''Another strategy exist using df.describe()'''
#set true for every deuplicated value
X_Bool = X.duplicated(keep = False)
#Result : a series of bool, true for every dulpicated value

#Check if there is any True in the series
print(any(X_Bool))                     
# Result : Prints False, Hence no repeatation

#remove the col
Uber = Uber.iloc[:,1:6]
#Result : ReqID is sliced from the dataset



#Removing the Drop timestamp
#Removing the Driver id
#As there is no reqment of that column
Uber = Uber[["Pickup point","Status","Request timestamp"]]
#Result : Dataset with "Pickup point","Status","Request timestamp"



#Removing month, day, year from the time stamps and getting a single format
#month and year are same
#days is linear
X = Uber["Request timestamp"] 
X = pd.to_datetime(X) #converting to numpy datetime type dtype('<M8[ns]')
X = X.dt.strftime('%S:%M:%H') #converting the timetsamp to ss:mm:hh
Uber["Request timestamp"] = X
#Result : Dataset with converted timestamp ss:mm:hh

"""Uni analysis"""
#Describe the dataset
Uber.describe()
#Result : Shows te count,unique values,etc of the datafraem
Uber["Pickup point"].value_counts()
Uber["Status"].value_counts()
Uber["Request timestamp"].value_counts()

#Uber["Pickup point"].plot.hist(bins=5) // this will not work if the seried or dataframe is not numeric data
Uber["Pickup point"].apply(pd.value_counts).plot.hist(bins=3)
Uber["Status"].apply(pd.value_counts).plot.hist(bins=2)
Uber["Request timestamp"].plot.hist(bins=10)
Uber["Request timestamp"].apply(pd.value_counts).plot(style = "k.")
