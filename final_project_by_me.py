# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:04:41 2020

@author: abm
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
#Get the stock quote 
df = pd.read_csv(r"C:\Users\abm\Downloads\NSE-TATAGLOBAL.csv") 
#Show the data 
print("\n\tPress 'Enter' key to view first 5 data of NSE-TATAGLOBAL.csv file ")
input()
a = df.head(5)
print(a)
print("\n\n\tPress 'Enter' key to view shape of NSE-TATAGLOBAL.csv file ")
input()
b = df.shape
print(b)

print("\n\n\tPress 'Enter' key to view GRAPH between DATE and CLOSING_PRICE ")
input()
#Visualize the closing price history
plt.figure(figsize=(16,8))
plt.title('Close Price History')
plt.plot(df['Close'])
plt.xlabel('Date',fontsize=18)
plt.ylabel('Close Price USD ($)',fontsize=18)
plt.show()


#Create a new dataframe with only the 'Close' column
data = df.filter(['Close'])
#Converting the dataframe to a numpy array
dataset = data.values
avg = 0

#average of a stream of data
n = len(dataset)
def getAvg(prev_avg, x, n):
    return((prev_avg * n + x)/(n+1))

for i in range(n):
    avg = getAvg(avg, dataset[i], i)
    

    
#Create a new dataframe with only the 'Open' column
data = df.filter(['Open'])
#Converting the dataframe to a numpy array
dataset_Open = data.values

#Create a new dataframe with only the 'High' column
data = df.filter(['High'])
#Converting the dataframe to a numpy array
dataset_High = data.values

#Create a new dataframe with only the 'Low' column
data = df.filter(['Low'])
#Converting the dataframe to a numpy array
dataset_Low = data.values

#Create a new dataframe with only the 'Last' column
data = df.filter(['Last'])
#Converting the dataframe to a numpy array
dataset_Last = data.values


print("\n\n\n\tPress 'Enter' key to view PREDICTED and ACTUAL Stock Values of NSE-TATAGLOBAL company. ")
input()
#for i in range(n):    
#    a=[(g-h)/20 for g,h in zip(dataset_High,dataset_Low)]
#    psp = dataset_Last+ a -0.1
#    print(psp)
pred_v = 1    
def pred_value(pred_v, x, n, l):
    return(((pred_v) - n + x)/(20)+l)

for i in range(n):
    pred_v = pred_value(pred_v, dataset_High[i],dataset_Low[i],dataset_Last[i])
    asd = float(pred_v)
    psp = "{:.3f}".format(asd)
    print("  Predicted value: [",psp,"]","\tActual value : ",dataset[i])
print("\n\n\n\t\t==================================")
print("\t\t| Press 'Enter' key to __EXIT__. |")
print("\t\t==================================")
input()  