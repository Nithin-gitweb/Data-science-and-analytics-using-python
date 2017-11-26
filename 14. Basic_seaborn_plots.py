import seaborn as sb
import matplotlib.pyplot as plt
#Loading a template data set
var = sb.load_dataset('tips')
print(var.head(10)) #Data set is generated
#Generating a distribution plot
pl1 = sb.distplot(var['total_bill'],kde=True)
plt.show() #Distribution plot graph is generated
#Generating a joint plot
pl2 = sb.jointplot(x='tip',y='total_bill',data=var,kind='hex')
plt.show()
#Pairplot generation
pl3 = sb.pairplot(var,hue='size')
plt.show()
#generating a rug_plot
pl4 = sb.rugplot(var['tip'])
plt.show()
#Genrating a KDE plot
pl5 = sb.kdeplot(var['size'])
plt.show()




