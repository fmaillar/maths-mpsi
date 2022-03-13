# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 20:16:11 2022

@author: e_fmaill
"""

import numpy as np
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

theta = np.linspace(-np.pi/2, np.pi/2, 1000)
r = np.cos(theta) + np.cos(3*theta)

fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.set_aspect('equal', adjustable='box')
# ax.axhline(y=0, color='k')
# ax.axvline(x=0, color='k')
# ax.set_aspect(1)
# ax.set_xlim(-0.5,2.5)
# ax.set_ylim(-1,1)

#plt.axes(projection = 'polar')
#fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
xT=plt.xticks()[0]
xL=['0',r'$\frac{\pi}{4}$',r'$\frac{\pi}{2}$',r'$\frac{3\pi}{4}$',\
    r'$\pi$',r'$\frac{5\pi}{4}$',r'$\frac{3\pi}{2}$',r'$\frac{7\pi}{4}$']
plt.xticks(xT, xL)
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
ax.set_rlabel_position(+60)  # Move radial labels away from plotted line
ax.grid(True)

ax.plot(theta+(r<0)*np.pi, np.abs(r))

plt.grid('True', which='both')
plt.savefig('courbepolaire.png')
plt.close('all')