import matplotlib.pyplot as mtp
import seaborn as sb
import numpy as np

var = sb.load_dataset('tips')
print(var.head(2)) #A dataset is created
#CATEGORICAL PLOTS:
#1. Barplot
sb.barplot(x = 'sex',y = 'tip',data=var)
mtp.show()
#2. Estimator of barplot
#I. std dev
sb.barplot(x = 'sex',y = 'tip',data=var,estimator=np.std)
mtp.show()
#2. Count plot
sb.countplot(x = 'total_bill',data = var)
mtp.show()
#3. Boxplot
sb.boxplot(x = 'day', y = 'total_bill',data = var,hue = 'sex')
mtp.show()
#4. Violin plot
sb.violinplot(x = 'sex', y = 'total_bill', data = var, hue = 'day')
mtp.show()
#5. Stripplot
sb.stripplot(x = 'sex', y = 'total_bill', data = var, hue = 'smoker',jitter=True)
mtp.show()
#6. swarmplots
sb.swarmplot(x = 'smoker', y = 'total_bill', data = var, hue = 'sex')
mtp.show()
#7. factorplot
sb.factorplot(x = 'time',y='size',data=var,kind='box')
mtp.show()
