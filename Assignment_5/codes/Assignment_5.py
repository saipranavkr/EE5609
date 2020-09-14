#!/usr/bin/env python
# coding: utf-8

# In[6]:


#! /usr/bin/python3
import numpy as np

x1 = np.array([0,3,2], dtype=float)
y = np.array([0,0,4], dtype = float)
x2 = np.array([0,3,5], dtype = float)

def area(x,y):
    return 0.5*((x[0]*(y[1]-y[2]))+(x[1]*(y[2]-y[0]))+(x[2]*(y[0]-y[1])))

Area1 = area(x1,y)
Area2 = area(x2,y)

if Area1 == Area2:
    print("Areas of triangles with same bases between two parrallel lines are equal")

