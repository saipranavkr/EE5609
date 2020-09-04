#!/usr/bin/env python
# coding: utf-8

# In[25]:


#! /usr/bin/python3
import numpy as np

# Initialising arrays as given in the (i) problem
XplusY = np.array([[7,0],
                  [2,5]])
XminusY = np.array([[3,0],
                   [0,3]])
X2 = XplusY + XminusY

# Finding X value
X_1 = X2//2
# Finding Y value
Y_1 = XplusY - X_1

print("(i)")
print("X=",X_1)
print("Y=",Y_1)
print("-------------------")

# Initialising arrays as given in the (ii) problem
X2plusY3 = np.array([[2,3],
                    [4,0]])
X3plusY2 = np.array([[2,-2],
                    [-1,5]])

# Multiplying 1st matrix by 3 and 2nd matrix by 2
X6plusY9 = X2plusY3 * 3
X6plusY4 = X3plusY2 * 2

Y5 = X6plusY9 - X6plusY4

#Finding Y value
Y_2 = Y5/5
Y3 = Y_2 * 3
X2 = X2plusY3 - Y3

#Finding X value
X_2 = X2/2

print("(ii)")
print("X=",X_2)
print("Y=",Y_2)

