#Missing data
import numpy as np
import pandas as pd

dic = {'A':[1,np.nan,3],'B':[np.nan,5,np.nan],'C':[np.nan,6,7],'D':[8,9,0]}
arr = pd.DataFrame(dic)
print(arr) #Printing a mere data frame
print(arr.dropna()) #Dropping all those rows which has null
print(arr.dropna(axis = 1)) #Dropping all colons which are null
print(arr.dropna(thresh=2)) #Dropping rows which has 2 null values
print(arr.fillna(value='PODA DEI')) #Filling all those null with a string
print(arr['A'].fillna(value=arr['A'].mean())) #Filling all those null with mean of each colomn

#Groupby functions
dic2 = {'house':['GRYF','GRYF','RAVEN','RAVEN','HUFF','HUFF','SLYTH','SLYTH'],'Students':['Harry','Hermione','Rowena','Helena','Oliver',
        'wood','Draco','Snape'], 'points': [300,280,260,320,140,172,196,200]}
arr6 = pd.DataFrame(dic2)
print(arr6) #A data frame using the above dictionary is created
arr7 = arr6.groupby('house') #Groupby function with respect to house is performed
print(arr7) #Not printed coz a mere group by can't be displayed. hence only type and address is printed
print(arr6.groupby('house').mean())
print(arr6.groupby('house').describe().transpose())
