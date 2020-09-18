#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import norm
import math


# In[15]:


x = np.linspace(-5,10,100)
y_1 = 0.5*x-3 # straight line 1
y_2 = -0.33*x-2 # straighe line 2
plt.plot(x, y_1, '-m', label='x-2y-6=0')
plt.title('Graph of 2y=3x+7')
plt.plot(x, y_2, '-c', label='x+3y+6=0')
plt.title('Graph of two straight lines')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.grid()
plt.show()


# In[ ]:




