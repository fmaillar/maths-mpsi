# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 15:22:34 2022

@author: e_fmaill
"""

import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

center = (0.0, 0.0)
def TraceModule(x, y, ax):
    p = [center, (x, y)]
    ax.plot(*zip(*p))        
data = [1+1j, 1-1j, -1+1j]
annotations = [r'$z_1$', r'$z_2$', r'$z_3$']
annotations_mod = [r'$|z_1|$', r'$|z_2|$', r'$|z_3|$']
# extract real part
x = [ele.real for ele in data]
# extract imaginary part
y = [ele.imag for ele in data]
#
fig, ax = plt.subplots()
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.scatter(x, y)
plt.ylabel('$\Im(z)$')
plt.xlabel('$\Re(z)$')
eps = 0.1
for i, label in enumerate(annotations):
    ax.annotate(label, (x[i], y[i]))
for i, label in enumerate(annotations_mod):
    TraceModule(x[i], y[i], ax)
    ax.annotate(label, (0.5*x[i]+eps, 0.5*y[i]+eps))
plt.grid('True', which='both')
plt.savefig('module_complexe.png')
plt.close()