import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

df3 = pd.read_csv('df3c.csv')
print(df3.info())
print(df3.head(5))
df3.plot.scatter(x='A',y = 'B',figsize = (12,3),s=50,c='red',edgecolor = 'black')
plt.show() #Scatter plot of A alog x and B along y axis
plt.style.use('ggplot')
df3['A'].plot(kind = 'hist',bins = 30,edgecolor = 'black') #GEnerates a histogram plot for column A
plt.show()
df3.plot.box(x='A',y='B') #Box plot for A along x and B along y
plt.show()
df3['A'].plot.kde(linewidth = 2) #Generates a KDE plot
plt.show()

