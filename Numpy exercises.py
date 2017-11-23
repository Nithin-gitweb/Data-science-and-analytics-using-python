import numpy as np
arr1 = np.ones(10)#Array of 10 ones
arr2 = np.zeros(10) #Array of 10 zeros
print(arr1)
print(arr2)
arr3 = 5 * arr1 #Array of 10 fives
print(arr3)
arr4 = np.arange(10,51) #Array of 10 to 51
print(arr4)
arr5 = []
for i in arr4:
    if i%2 == 0:
        arr5.append(i)
print(arr5) #Array of even from 10 to 51
arr6 = np.arange(0,9)
arr6 = arr6.reshape(3,3)#3x3 array of 0 to 8
print(arr6)
arr7 = np.eye(4) #identity matrix
print(arr7)
arr8 = np.random.rand(2) #Random between 0 to 1
print(arr8)
arr9 = np.random.randn(25) #25 random numbers in standard distribution
print(arr9)
arr10 = np.arange(110)
arr10 = arr10.reshape(11,10)
arr10 = arr10 / 100
print(arr10) # creating 0.01, 0.02, 0.03 2d array
arr11 = np.linspace(0,1,20)
print(arr11) #Linear equal points between 0 to 1
arr12 = np.arange(10)
arr12 = arr12.reshape(2,5)
print(arr12)
print(np.sum(arr12)) #sum of elements in an 2d array
print(np.std(arr12)) #Std dev of 2d array
print(np.sum(arr12,axis=0)) #Sum of a row in 2d array
print(np.sum(arr12,axis=1)) #Sum of a colomn in a 2d array




