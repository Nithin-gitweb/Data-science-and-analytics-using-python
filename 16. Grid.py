import matplotlib.pyplot as plt
import seaborn as sb
#iris dataset
var = sb.load_dataset('iris')
print(var.head(5))
var2 = sb.load_dataset('tips')
print(var2.head(5))
#Pair grid
obj1 = sb.PairGrid(var)
obj1.map_diag(sb.distplot)
obj1.map_lower(plt.scatter)
obj1.map_upper(sb.kdeplot)
plt.show()
#Facet grid
obj2 = sb.FacetGrid(data=var2,row='smoker',col='sex')
obj2.map(sb.barplot,'total_bill','tip')
plt.show()
