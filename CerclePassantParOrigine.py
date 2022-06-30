# -*- coding: utf-8 -*-
"""
Created on Sat May  7 11:41:46 2022.

@author: e_fmaill
"""
import matplotlib.pyplot as plt
import numpy as np
import geometry as geom
import angle_annotation as an

NewGreen = '#2ca02c'
NewBlue = '#1f77b4'
NewOrange = '#ff7f0e'

Omegax, Omegay = 3, 2
Omega = geom.Point(Omegax, Omegay)
Origine = geom.Point(0, 0)
R = geom.Point.distance(Omega, Origine)
phi = np.arctan(Omegay/Omegax)

theta = np.pi/2.35
rho = 2*R*np.cos(theta-phi)

Mx, My = rho*np.cos(theta), rho*np.sin(theta)
M = geom.Point(Mx, My)
H = geom.Point(Mx/2, My/2)

OM = [Origine.coord(), M.coord()]
OOmega = [Origine.coord(), Omega.coord()]
OmegaM = [Omega.coord(), M.coord()]
OmegaH = [Omega.coord(), H.coord()]

theta2 = np.linspace(0, 2*np.pi, 100)
x1 = R*np.cos(theta2-phi)+Omegax
x2 = R*np.sin(theta2-phi)+Omegay

fig, ax = plt.subplots(1)

ax.plot(x1, x2)
ax.set_aspect(1)
ax.plot(Origine.xabs, Origine.yord, M.xabs, M.yord, Omega.xabs, Omega.yord,
        H.xabs, H.yord,
        marker='+', color='black')
ax.annotate('$M$', (M.xabs, M.yord), fontsize=12)
ax.annotate('$\\Omega$', (Omega.xabs, Omega.yord), fontsize=12)
ax.annotate('$O$', (Origine.xabs, Origine.yord), fontsize=12,
            xytext=(-0.5, -0.5))
ax.annotate('$H$', (H.xabs, H.yord), fontsize=12)
ax.annotate('$\\rho/2$', (H.xabs/2, H.yord/2+0.5), fontsize=12)
ax.annotate('$R$', (Omega.xabs/2+0.3, Omega.yord/2), fontsize=12)
ax.plot(*zip(*OM), color=NewOrange)
ax.plot(*zip(*OOmega), *zip(*OmegaM), color='black')
ax.plot(*zip(*OmegaH), ls='--', color=NewGreen)

p = [(2, 0), (Omegax, Omegay), (Mx, My)]

am = an.AngleAnnotation(Origine.coord(), p[0], p[1], ax=ax,
                        text=r"$\phi$", color=NewBlue,
                        text_kw=dict(fontsize=12, color=NewBlue))
am2 = an.AngleAnnotation(Origine.coord(), p[1], p[2], ax=ax,
                         text=r"$\theta-\phi$", color=NewOrange,
                         textposition="outside",
                         text_kw=dict(fontsize=12, color=NewOrange))

# plt.xlim(-1.25, 1.25)
# plt.ylim(-1.25, 1.25)

plt.grid(which='both')
plt.tight_layout()
plt.savefig('Equation_polaire_cercle', dpi=160)
