import numpy as np
#Basic Matrix array using numpy
arr = range(3)
arr2 = [[arr],[arr],[arr]]
print(np.array(arr2))
#arange function to generate list/array
print(np.arange(0,10,2))
#Array of zeros and ones as it contributes to binary
arr3 = np.zeros(4)#matrix array
print(arr3)
arr4 = np.ones(4)#vector array
print(arr4)
#Line space function
arr5 = np.linspace(0,10,25)
print(arr5)
#eye function
arr6 = np.eye(4) #Always a multi dimensional
#Rand and randn function
arr7 = np.random.rand(3,3) #multi dimensional random uniform distribution array
print(arr7)
arr8 = np.random.randn(3,3)#Vector array of standard distribution
print(arr8)
finalarray = np.random.randint(5,25,16)
print(finalarray)#Random array generation
print('The min, max, min index and max index are \n')
print(finalarray.min(),finalarray.max(),finalarray.argmin(),finalarray.argmax())
arr9 = finalarray.reshape(4,4) #Reshaping final array from vector to matrix
print(arr9)
