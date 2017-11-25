import numpy as np
import pandas as pd

file = pd.read_csv('sample.csv')
print(file)
print(type(file))
dic1 = {'A':['a0','a1','a2'],'B':['b0','b1','b2'],'C':['c0','c1','c2']}
dic2 = {'D':['d0','d1','d2'], 'E':['e0','e2','e3'],'F':['f0','f1','f2']}
arr1 = pd.DataFrame(dic1,index=[1,2,3])
arr2 = pd.DataFrame(dic2,index=[1,2,3])
arr1.to_csv('sample2.csv',index=True)