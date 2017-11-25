import pandas as pd
import numpy as np

obj = pd.read_csv('ecom.csv')
print(obj.head()) #Checks the head of the csv file
print(len(obj.columns)) #Number of columns
print(obj.index) #number of rows
print(obj['Purchase Price'].mean()) #Average purchase price
print(obj['Purchase Price'].min()) #Lowest Purchase price
print(obj['Purchase Price'].max()) #Highest Purchase price
print(obj[obj['Language'] == 'en']['Language'].nunique()) #Number of people who opted for english as theier choice of language
print(obj[obj['Job'] == 'Lawyer']['Job'].count()) #Number of people who work as advogate
#Number of persons who made purchases at AM and PM
apm = obj['AM or PM'].value_counts()
print(apm)
print(obj['Job'].value_counts().head(5)) #Top 5 common job titles
#Get the purchase price for the lot number 90 WT
print(obj[obj['Lot']=='90 WT']['Purchase Price'])
#Number of people who made purchases using American Express and above $95
seq = (obj[obj['CC Provider'] == 'American Express']['Address'].count()) & (obj[obj['Purchase Price']>95]['Address'].count())
print(seq) #Conditional Indexing
#Number of people whose credit card expires in 2025
print(sum(obj['CC Exp Date'].apply(lambda x:x[3:]==25))) #Appy condition
print(obj['Email'].apply(lambda mail: mail.split('@')[1]).value_counts().head(5)) #Top 5 mail server providers


