import numpy as np
import pandas as pd

#Creating a data frame
dic1 = {'A':['a0','a1','a2'],'B':['b0','b1','b2'],'C':['c0','c1','c2']}
dic2 = {'D':['d0','d1','d2'], 'E':['e0','e2','e3'],'F':['f0','f1','f2']}
arr1 = pd.DataFrame(dic1,index=[1,2,3])
arr2 = pd.DataFrame(dic2,index=[1,2,3])
print(arr1)
print(arr2)
print(arr1['C'].unique()) #unique
print(arr2['F'].nunique()) #nunique
print(arr2['E'].value_counts()) #value counts
arr5 = arr2['D'].apply(lambda x:x + ' Nithin') #apply
print(arr5)
print(arr1.columns) #Column function
print(arr1.index) #Row function
print(arr2.sort_values(['E'])) #Sort values
print(arr1.isnull()) #Checks for null

