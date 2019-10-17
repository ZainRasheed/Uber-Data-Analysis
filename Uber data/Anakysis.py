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



#Removing month, year from the time stamps and getting a single time format
#month and year are same in every row hance removing it
#days is moved to a new column 
X = Uber["Request timestamp"]

#Identifying the indexes from the series for different time formats
X_Bool_type_m = X.str.contains("/")
#Getting a index boolean series for dd/mm/yyyy hh:mm format
X_Bool_type_d = X.str.contains("-")
#Getting a index boolean series for dd-mm-yyyy hh:mm:ss format

X = pd.to_datetime(X) #converting to numpy datetime type dtype('<M8[ns]')
temp_date_col = X.copy() #copying the column to another vairable

#getting the dates out from other both date formats 
temp_date_col[X_Bool_type_m] = X[X_Bool_type_m].dt.strftime('%m')
#got the date from the dd/mm/yyyy hh:mm format, but it was placed in the month position
temp_date_col[X_Bool_type_d] = X[X_Bool_type_d].dt.strftime('%d')
#got the date from the dd-mm-yyyy hh:mm:ss format, but it was placed in the month position

#adding a new column
Uber["Request date"] = temp_date_col
#Request date column added



 #Segregated column for date
X = Uber["Request timestamp"]
X = pd.to_datetime(X)
X = X.dt.strftime('%H:%M:%S') #converting the timetsamp to ss:mm:hh
Uber["Request timestamp"] = X
#Result : Dataset with converted timestamp ss:mm:hh



#categorizing time
plt.scatter(Uber["Request time"], Uber["Request date"], s=10, c='b', marker="s", label='first')
plt.legend(loc='upper left');
plt.show()






"""Uni analysis"""
#Describe the dataset
Uber.describe()
"""
Result : Shows te count,unique values,etc of the dataframe
       Pickup point          Status Request timestamp Request date
count          6745            6745              6745         6745
unique            2               3              5618            5
top            City  Trip Completed    11/7/2016 9:40           15
freq           3507            2831                 6         1381
"""

#count of types
Uber["Pickup point"].value_counts()
"""
City       3507
Airport    3238
Name: Pickup point, dtype: int64
"""

Uber["Status"].value_counts()
"""
Trip Completed       2831
No Cars Available    2650
Cancelled            1264
Name: Status, dtype: int64
"""

Uber["Request timestamp"].value_counts()
"""
11/7/2016 9:40         6
11/7/2016 8:37         6
                      ...
15-07-2016 19:49:13    1
14-07-2016 10:06:29    1
Name: Request timestamp, Length: 5618, dtype: int64
"""
#sns.heatmap(Uber["Request timestamp"])

#Uber["Pickup point"].plot.hist(bins=5) // this will not work if the seried or dataframe is not numeric data
#Histogram to see the distributions
Uber["Pickup point"].apply(pd.value_counts).plot.hist()
Uber["Status"].apply(pd.value_counts).plot.hist(bins=2)
#Uber["Request timestamp"].plot.hist(bins=10)
#Uber["Request timestamp"].apply(pd.value_counts).plot(style = "k.")