# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:58:45 2022

@author: e_fmaill
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from numpy.random import seed, random_sample
# from mpl_toolkits.mplot3d import Axes3D
mpl.rcParams['text.usetex'] = True

NewGreen = '#2ca02c'
NewBlue = '#1f77b4'
NewOrange = '#ff7f0e'

seed(29078)

N = 25
a = 1
Sup = 2
c = 3
y = np.zeros(N)
x = (c-a)*random_sample(N) + a

Majorant = x > Sup

t = np.linspace(np.min(x)-0.1, np.max(x)+0.1, 100)
y2 = np.zeros(100)

fig, ax = plt.subplots()
# ax.set_xlim([a, b])
ax.axes.yaxis.set_visible(False)
ax.axes.xaxis.set_visible(False)
ax.plot(t, y2, color='grey')
ax.scatter(x[Majorant], y[Majorant], s=30, marker='>', c=NewOrange,
           label='Ensemble des majorant de $A$')
ax.scatter(x[~Majorant], y[~Majorant], s=30, marker='D', c=NewBlue,
           label='Ensemble $A$')
ax.scatter(Sup, 0, s=90, marker="*", c=NewGreen, label='$\\sup A$')
plt.legend(loc='best')
# plt.show()
plt.savefig("BorneSup.png", dpi=200)
