import numpy as np
import pandas as pd
#Creating a Dataframe object
arr1 = np.random.randn(5,4)
arr1 = np.array(arr1)
dfo = pd.DataFrame(arr1,['A','B','C','D','E'],['W','X','Y','Z'])
print(dfo)
#Indexing with respect to colomn
arr2 = dfo['W']   #Single colomn addressing
arr3 = dfo[['Y','Z']] #Multiple colomn addressing
print(arr2)
print(arr3)
#Creating a new colomn
dfo['N'] = dfo['X'] + dfo['Y']
print(dfo['N'])
#Removing a colomn
print(dfo)
dfo.drop('N',axis=1,inplace=True)
print(dfo) #To show whether the changes has been made to the original dfo
#Indexing a row
arr5 = dfo.loc[['A','B'],['X','Y']]
print(arr5) #Indexing filtered row and colomn using loc
arr6 = dfo.iloc[2]#Indexing using index number by iloc function
print(arr6)
###########END OF PART 1 #####################
#Conditional selection
booldfo = dfo > 0 #Boolean condition data frame
print(booldfo)
print(dfo[booldfo]) #Passing boolean condition as a parameter in dataframe returns only *VALUES* which are true
print(dfo['X']<0) #Condition for a specific row / colomn
#Multiple conditions
muldfo = (dfo['X']>0) & dfo['Z'] < 0
print(muldfo)
ind = dfo.reset_index()
print(ind)
ind2 = dfo.set_index(['X','Y'])
print(ind2)
############END OF PART 2#############
#Multi indexing and hierarchy
out = ['A1','A1','B1','B1','C1','C1']
ins = [1,2,1,2,1,2]
insouts = list(zip(out,ins))
insouts = pd.MultiIndex.from_tuples(insouts) #Generating a multi index pre requisite as a list of tuples
print(insouts)
arr7 = pd.DataFrame(np.random.randn(6,3),insouts,['X','Y','Z']) #Forming an multi index data frame
print(arr7)
print(arr7.loc['B1'].loc[2,'X']) #Addressing using loc and iloc function
arr7.index.names = ['Group','Entry'] #Declaring names for indeices
print(arr7.xs(2,level='Entry')) #Addressing using cross sectional function (xs)
############END OF PART 3###########
