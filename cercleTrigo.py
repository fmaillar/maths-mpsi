# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 10:25:39 2022

@author: e_fmaill
"""

import numpy as np
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import angle_annotation as an

theta = np.linspace(0, 2*np.pi, 360)

r = 1

a = r*np.cos(theta)
b = r*np.sin(theta)

center = (0.0, 0.0)
theta0 = 0.2*np.pi
x0 = r*np.cos(theta0)
y0 = r*np.sin(theta0)
tan0 = y0/x0


#x = np.linspace(0, 1./np.tan(theta0),100)
#y = np.tan(theta0)*x

p1 = [center, (1/tan0, np.sign(y0))]   #utheta
p2 = [(0, y0), (x0, y0)]    #cos theta
p3 = [(x0, 0), (x0, y0)]    #sin theta
p5 = [(0,1), (1/tan0, np.sign(y0))]    #cotan theta
p4 = [(1,0), (1, tan0)]    #tan theta
if (x0 < 0 and y0>0):
    p6 = [center, (1, tan0)]
if (y0<0 and x0>0):
    p6 = [center, (-1, -tan0)]
fig, ax = plt.subplots()
fig.canvas.draw()
ax.set_aspect(1)
#ax.set_aspect('equal', adjustable='box')
ax.plot(a,b)
#ax.plot(x,y, color='gray')

ax.plot(*zip(*p1))
ax.plot(*zip(*p2))
ax.plot(*zip(*p3))
ax.plot(*zip(*p4))
ax.plot(*zip(*p5))
if (x0 < 0 and y0>0) or (y0<0 and x0>0):
    ax.plot(*zip(*p6), '--')
    
eps = 1./20

if theta0%(2*np.pi) < np.pi :
    am = an.AngleAnnotation(center, (1,0), p1[1], ax=ax, size=100, text=r"$\theta$")
else:
    am = an.AngleAnnotation(center, p1[1], (1,0), ax=ax, size=100, text=r"$\theta$")
    
ax.text(x0/2,y0+eps, r'$\cos \theta$', ha='center', usetex=True)
ax.text(x0/2*np.sign(y0),1+eps, r'$1/{\tan \theta}$', ha='center', usetex=True)
ax.text(x0-eps,y0/2, r'$\sin \theta$', ha='center', rotation='vertical', usetex=True)
ax.text(1+2*eps,y0, r'$\tan \theta$', ha='center', rotation='vertical', usetex=True)
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.grid('on')
plt.show()
plt.savefig('CercleTrigo')