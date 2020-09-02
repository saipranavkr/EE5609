#!/usr/bin/env python
# coding: utf-8

# In[2]:


## ! /usr/bin/python3
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#Initialising arays for storing 5 coordinates
X_axis = [0]*5
Y_axis = [0]*5
Z_axis = [0]*5

#Calculating 5 points which lie on the line from the parametric form 
for t in range(5):
    X_axis[t] = 3*t + 5
    Y_axis[t] = 7*t - 4
    Z_axis[t] = 2*t + 6
    
#A 3D empty axis to plot the points
graph_basic = plt.axes(projection='3d')

#Plot the line in the 3D system using the defined points
graph_basic.plot3D(X_axis,Y_axis,Z_axis,label='Fig:A straight line in 3D space')


# In[ ]:




