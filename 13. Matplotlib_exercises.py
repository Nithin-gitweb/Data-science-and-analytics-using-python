import numpy as np
import matplotlib.pyplot as plt
import time as t
x = np.arange(0,100)
y = x*2
z = x**2
#Ex 01. To create a chart object, set axes to it and plot the x and y values
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_xlabel('X axis')
ax.set_ylabel('Y Axis')
ax.set_title('Graph one')
fig.show()
t.sleep(3)
#To create a figure object and put two axes objects in it, one ranging from [0,0,1,1] and the other [0.2,0.5,0.2,0.2]. Plotiing not necss
fig2 = plt.figure()
ax2 = fig2.add_axes([0,0,1,1])
ax3 = fig2.add_axes([0.2,0.5,0.2,0.2])
fig2.show()
t.sleep(3)
#Now, plot the above graph with x,y or y,z
ax2.plot(x,y)
ax3.plot(y,z)
fig2.show()
t.sleep(3)
#Create another graph object for loc [0,0,1,1] and [0.2,0.5,0.4,0.4]
fig3 = plt.figure()
ax4 = fig3.add_axes([0,0,1,1])
ax5 = fig3.add_axes([0.2,0.5,0.4,0.4])
ax4.plot(x,y)
ax4.plot(x,z)
ax5.plot(y,z)
ax5.plot(z,y)
fig3.show()
t.sleep(3)
#Create a sub plot with one row and two colomns
fig4, ax2 = plt.subplots(nrows=1,ncols=2)
fig4.show()
t.sleep(3)
ax2[0].plot(x,y,color = 'Purple',lw = 2, alpha = 1.5, ls = '-.',marker = '+',markersize = '15', markerfacecolor = 'Red')
ax2[1].plot(y,x,color = 'Red',lw = 2, alpha = 1.5, ls = '-.',marker = 'o',markersize = '15', markerfacecolor = 'Purple')
fig2.show()
t.sleep(3)

