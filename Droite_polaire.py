# -*- coding: utf-8 -*-
"""
Created on Tue May 17 12:15:39 2022

@author: e_fmaill
"""

import matplotlib.pyplot as plt
import numpy as np
import geometry as geom
import angle_annotation as an

NewGreen = '#2ca02c'
NewBlue = '#1f77b4'
NewOrange = '#ff7f0e'

Origine = geom.Point(0, 0)
Hx, Hy = 3, 2
H = geom.Point(Hx, Hy)
R = Origine.distance(H)
phi = np.arctan(Hy/Hx)

theta = np.pi/2.3
rho = R/np.cos(theta-phi)

Mx, My = rho*np.cos(theta), rho*np.sin(theta)
M = geom.Point(Mx, My)

eps = 0.7
theta2 = np.linspace(phi-np.pi/2+eps, phi+np.pi/2-eps, 100)
M2x = R/np.cos(theta2-phi)*np.cos(theta2)
M2y = R/np.cos(theta2-phi)*np.sin(theta2)

OM = [Origine.coord(), M.coord()]
OH = [Origine.coord(), H.coord()]

fig, ax = plt.subplots(1)
ax.set_aspect(1)
ax.plot(*zip(*OM), color=NewOrange)
ax.plot(*zip(*OH), color=NewBlue, ls='--')
ax.plot(M2x, M2y)
ax.annotate('$M$', (M.xabs, M.yord), fontsize=12)
ax.annotate('$H$', (H.xabs, H.yord), fontsize=12)
ax.annotate('$O$', (Origine.xabs, Origine.yord), fontsize=12,
            xytext=(-0.25, -0.25))
ax.plot(Origine.xabs, Origine.yord, M.xabs, M.yord, H.xabs, H.yord,
        marker='+', color='black')
p = [(2, 0), (Hx, Hy), (Mx, My)]
am = an.AngleAnnotation(Origine.coord(), p[0], p[1], ax=ax,
                        text=r"$\phi$", color=NewBlue,
                        text_kw=dict(fontsize=12, color=NewBlue))
am2 = an.AngleAnnotation(Origine.coord(), p[1], p[2], ax=ax,
                         text=r"$\theta-\phi$", color=NewOrange,
                         textposition="outside",
                         text_kw=dict(fontsize=12, color=NewOrange))
ax.annotate('$R$', (H.xabs/2+0.3, H.yord/2), fontsize=12)
ax.annotate('$\\rho$', (M.xabs/2-0.3, M.yord/2+0.3), fontsize=12)

plt.grid(which='both')
plt.tight_layout()
plt.savefig('Equation_polaire_droite', dpi=160)
