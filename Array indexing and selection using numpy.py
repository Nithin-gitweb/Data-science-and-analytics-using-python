import numpy as np
#Declare an array
arr1 = np.arange(10)
print(arr1)
slice = arr1[3:8]
slice[:] = 23
print(slice)
print(arr1)
#Since slice depends on the original array, any changes to slice will dorectly affect arr.
#To overcome this we use copy function
arr2 = np.arange(10)
slice1 = arr2.copy()
slice1[:] = 23
print(slice1)
print(arr2)
#The above problem of array dependency is now cleared here.

#ADDRESSING AN ARRAY
arr3 = np.arange(50)
arr3 = arr3.reshape(5,10)
print(arr3[1][3]) #Addressing by double bracket notation
print(arr3[1,3]) #Addressing by single bracket notation
print(arr3[1:3,4:6]) #Group addressing by single bracket notation