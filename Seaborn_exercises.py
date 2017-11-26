import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

var = sb.load_dataset('titanic')
print(var.head(2))
sb.set_style(style='whitegrid')
sb.jointplot(x='fare',y='age',data=var)
plt.show() #Replicates the titanic data as a scatter plot graph
sb.distplot(var['fare'])
plt.show() #Replicates the distribution plot with respect to fare
sb.boxplot(x='class',y = 'age',data=var,palette='coolwarm')
plt.show() #Replicates the box graph with respect to class along x and age along y axis
sb.swarmplot(x='class',y = 'age',data=var)
plt.show()#Replicates the swarm plot of titanic. class along x axis and age along y axis
sb.countplot(x = 'sex',data=var)
plt.show() #Replicating the bar plot in the exercise notes
tab1 = var.corr()
sb.heatmap(tab1,cmap='coolwarm') #Replicates the heatmap given in notebook
plt.title('titanic.corr()')
plt.show()
fp = sb.FacetGrid(data=var,col='sex')
fp.map(sb.distplot,'age')
plt.show() #Generates a replication of the given facetplot

