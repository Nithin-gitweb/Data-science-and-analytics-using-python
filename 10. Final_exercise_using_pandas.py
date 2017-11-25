import numpy as np
import pandas as pd

sal = pd.read_csv('Salaries_sample.csv')
print(sal.head(2)) #Finding the head for 2 rows
print(sal.info()) #Finding number of rows and colomns
print(sal['BasePay'].mean()) #finding the average base pay
print(sal['OvertimePay'].max()) #Finding the highest amount of overtime pay
ass = sal['EmployeeName'] == 'JOSEPH DRISCOLL'
print(sal[ass]['JobTitle']) #Joseph's Job Title
print(sal[ass]['TotalPayBenefits']) #How much does Joseph make including benefits
print(sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]['EmployeeName']) #Who earns the most
print(sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()]['EmployeeName']) #Who earns the least
ass3 = sal.groupby('Year').mean()
print(ass3['BasePay']) #Average of mean of base pay of all employers categorised by year
print(sal['JobTitle'].nunique()) #Number of job occurances
print(sal['JobTitle'].value_counts().head(5)) #Commonly occupied top 5 jobs
arr1 = sal[sal['Year']==2013]['JobTitle'].value_counts()==1
arr2 = sum(arr1)
print(arr2) #Jobs which occors only one time in 2013
print(sum(sal[sal['Year']==2012]['JobTitle'].value_counts()==1)) #number of job which occors only one time
#Those who work as chief
def is_chief(text):
    if 'chief' in text.lower().split():
        return True
    else:
        return False
doo = (sum(sal['JobTitle'].apply(lambda x:is_chief(x)))) #Prints the number of members who work as chief
print(doo)
