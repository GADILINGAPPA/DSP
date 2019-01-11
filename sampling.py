#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 21:16:40 2019

@author: rgukt
"""

import numpy as np
import matplotlib.pyplot  as plt
n=np.linspace(0,100,1000)
m=np.linspace(0,10,50)
f=input("enter fequency f:")
fs=input("enter samplefequency fs:")
x=np.sin(2*np.pi*n*(float(f))
y=np.sin(2*np.pi*m*(float(f)/float(fs)))
fig=plt.figure()
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)
ax1.plot(n,x)
ax2.stem(m,y)

