import numpy as np
import matplotlib.pyplot as mtp
import time
#Function_Method
x = np.linspace(1,5)
y = x**2
mtp.plot(x,y,label = 'Plotted') #A graph is plotted
mtp.subplot(1,3,1) #Subplot 1
mtp.plot(x,y)
mtp.subplot(1,3,3) #Subplot 2
mtp.plot(y,x)

mtp.show()

#OOP Method
fig = mtp.figure()
ax = fig.add_axes([0.1,0.1,0.3,0.5]) #Creating a plot inside the graph
ax2 = fig.add_axes([0.2,0.2,0.2,0.3]) #Creating a plot inside the graph
ax.plot(x,y) #Plotting the first created graph
ax2.plot(y,x) #Plotting the second created graph
fig.show()
time.sleep(2)
fig,ax = mtp.subplots(nrows=3,ncols=1) #Creating sub plotsd in the already created graph
for i in range(0,3): #Plotting the pub plots
    if i%2 == 0:
        ax[i].plot(x,y)
    else:
        ax[i].plot(y,x)
fig.show()
time.sleep(2)
#Figure size, aspect ratio and DPI
fig,ax2 = mtp.subplots(nrows=3,ncols=1)
for i in range(0,3):
    if i%2 == 0:
        ax2[i].plot(x,y,label = 'Mod to 0')
        ax2[i].legend(loc = 0)
    else:
        ax2[i].plot(y,x,label = 'Mod to 1')
        ax2[i].legend(loc = 0)

fig.show()
fig.savefig('Sample.jpg',dpi=100)


