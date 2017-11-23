import pandas as pd
import numpy as np

arr = range(10)
arr = np.array(arr)
arr2 = pd.Series(arr) #Passing numpy array in pandas
print(arr2)
arr3 = range(11,21)
arr3 = np.array(arr3)
arr4 = pd.Series(arr3) #Passing numpy array in pandas
print(arr4)
arr5 = arr2 + arr4
print(arr5)
