#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 21:33:56 2019

@author: rgukt
"""

import numpy as np
import matplotlib.pyplot  as plt
n=np.linspace(0,100,100)
f1=input("enter frequency f1:")
f2=input("enter frequency f2:")
x=np.sin(2*np.pi*n*f1)
y=np.sin(2*np.pi*n*f2)
z=x+y
fig=plt.figure()
ax1=fig.add_subplot(3,1,1)
ax2=fig.add_subplot(3,1,2)
ax3=fig.add_subplot(3,1,3)
ax1.plot(n,x)
ax2.plot(n,y)
ax3.plot(n,z)
