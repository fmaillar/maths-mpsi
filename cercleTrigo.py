# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 10:25:39 2022

@author: e_fmaill
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import angle_annotation as an

mpl.rcParams['text.usetex'] = True

theta0 = np.pi/3.
#
theta = np.linspace(0, 2*np.pi, 360)
r = 1
a = r*np.cos(theta)
b = r*np.sin(theta)
center = (0.0, 0.0)
theta0deg = round(180.0/np.pi*theta0)
x0 = r*np.cos(theta0)
y0 = r*np.sin(theta0)
tan0 = y0/x0
cotan0 = x0/y0
sec0 = 1./x0
csc0 = 1./y0
# x = np.linspace(0, 1./np.tan(theta0),100)
# y = np.tan(theta0)*x

# utheta
p1 = [center, (x0, y0)]
# cos theta
p2 = [(0, y0), (x0, y0)]
# sin theta
p3 = [(x0, 0), (x0, y0)]
# cotan theta
p5 = [(0,csc0), (x0, y0)]
# tan theta
p4 = [(x0,y0), (sec0, 0)]


# if (x0 < 0 and y0 > 0):
#   p6 = [center, (1, tan0)]

# if (y0 < 0 and x0 > 0):
#    p6 = [center, (-1, -tan0)]

fig, ax = plt.subplots()
fig.canvas.draw()
ax.set_aspect(1)
plt.xticks(np.arange(-2, 5, step=0.5))
plt.yticks(np.arange(-2, 5, step=0.5))

plt.xlim(-1.25, np.floor(sec0)+1.5)
plt.ylim(-1.25, np.floor(csc0)+0.5)


# ax.set_aspect('equal', adjustable='box')
ax.plot(a, b)
# ax.plot(x,y, color='gray')

ax.plot(*zip(*p1))
ax.plot(*zip(*p2))
ax.plot(*zip(*p3))
ax.plot(*zip(*p4))
ax.plot(*zip(*p5))
# if (x0 < 0 and y0 > 0) or (y0 < 0 and x0 > 0):
#     ax.plot(*zip(*p6), '--')

eps = 1./20

if theta0 % (2*np.pi) < np.pi:
    am = an.AngleAnnotation(center, (1, 0), p1[1], ax=ax, size=100,
                            text=r"$\theta$")
else:
    am = an.AngleAnnotation(center, p1[1], (1, 0), ax=ax, size=100,
                            text=r"$\theta$")
# sec
plt.annotate('', xy=(sec0, -eps), xytext=(0., -eps),
            arrowprops=dict(arrowstyle='<->', color='red'), va='center')
# csc
plt.annotate('', xy=(-eps, csc0), xytext=(-eps, 0.),
            arrowprops=dict(arrowstyle='<->', color='blue'), va='center')
# tan
plt.annotate('', xy=(x0+eps, y0+eps), xytext=(sec0+eps, eps), 
             arrowprops=dict(arrowstyle='<->', color='green'), va='center')
# cot
plt.annotate('', xy=(x0+eps, y0+eps), xytext=(eps, csc0+eps), 
             arrowprops=dict(arrowstyle='<->', color='grey'), va ='center')

ax.text(x0/2, y0-2*eps, r'$\cos \theta$', ha='center', usetex=True)
ax.text(x0-eps, y0/2, r'$\sin \theta$', ha='center', rotation='vertical',
        usetex=True)
ax.text(sec0/2*0.8, -3*eps, r'$\sec \theta$', ha='center', usetex=True)
ax.text(-2*eps, csc0/2, r'$\csc \theta$', ha='center', rotation='vertical', 
        usetex=True)
ax.text((x0+eps+eps)/2., (y0+eps+csc0+eps)/2., r'$\cot \theta$', ha='center', 
        usetex=True, rotation = -(90-theta0deg))
ax.text((x0+eps+sec0+eps)/2, (y0+eps+eps)/2., r'$\tan \theta$', ha='center', 
        usetex=True, rotation = -(90-theta0deg))

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.grid('on')
plt.savefig('CercleTrigo', dpi=200)
plt.close('all')
