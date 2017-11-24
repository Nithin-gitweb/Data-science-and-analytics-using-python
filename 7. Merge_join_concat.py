import numpy as np
import pandas as pd
#Creating two dataframe objects from a dictionary
dic1 = {'A':['a0','a1','a2'],'B':['b0','b1','b2'],'C':['c0','c1','c2']}
dic2 = {'D':['d0','d1','d2'], 'E':['e0','e2','e3'],'F':['f0','f1','f2']}
arr1 = pd.DataFrame(dic1,index=[1,2,3])
arr2 = pd.DataFrame(dic2,index=[1,2,3])
print(arr1)
print(arr2)
print(pd.concat([arr1,arr2])) #Concatination along colomn
print(pd.concat([arr1,arr2],axis=1)) #Concatenation along row
#Merging function
dic3 = {'A':['a0','a1','a2'],'B':['b0','b1','b2'],'C':['c0','c1','c2']}
dic4 = {'D':['d0','d1','d2'], 'E':['e0','e2','e3'], 'C':['c0','c1','c2']}
arr3 = pd.DataFrame(dic3)
arr4 = pd.DataFrame(dic4)
print(pd.merge(arr3,arr4,on='C')) #Merging done


