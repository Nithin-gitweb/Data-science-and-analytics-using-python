import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LogisticRegression,LinearRegression
df = pd.read_csv('train.csv')
df = pd.DataFrame(df)
print(df.info())
sb.jointplot(x = 'YearBuilt',y='YearRemodAdd',data=df,color='Red',kind='hex')
plt.show()
sb.barplot(x = 'SaleCondition',y = 'SalePrice', data=df)
plt.show()
sb.violinplot(x= 'YearBuilt',y = 'OverallCond', data=df)
plt.show()










