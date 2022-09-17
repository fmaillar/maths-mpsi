# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 18:32:00 2022

@author: e_fmaill
"""
import geometry as geo
import matplotlib.pyplot as plt

A = geo.Point(-1, 3.0)
B = geo.Point(5, 1)
C = geo.Point(1, 5)

u = C.vecteur(A)
vb = C.vecteur(B)

# print(u*vb)
# print(u.ortho(vb))

d1 = geo.Droite(C, A)
d2 = geo.Droite(C, B)

# print(d1.perpendiculaire(d2))

C1 = geo.Point(-4, 0)
L = 2
M1 = geo.Point(-1, 2)
M2 = geo.Point(1, 2)
M3 = geo.Point(1, -2)
M4 = geo.Point(-1, -2)

N1 = geo.homothety(L, C1, M1)
N2 = geo.homothety(L, C1, M2)
N3 = geo.homothety(L, C1, M3)
N4 = geo.homothety(L, C1, M4)

M_X = [M1.xabs, M2.xabs, M3.xabs, M4.xabs]
M_Y = [M1.yord, M2.yord, M3.yord, M4.yord]
N_X = [N1.xabs, N2.xabs, N3.xabs, N4.xabs]
N_Y = [N1.yord, N2.yord, N3.yord, N4.yord]

p1 = [(M1.xabs, M1.yord), (N1.xabs, N1.yord)]
p2 = [(M2.xabs, M2.yord), (N2.xabs, N2.yord)]
p3 = [(M3.xabs, M3.yord), (N3.xabs, N3.yord)]
p4 = [(M4.xabs, M4.yord), (N4.xabs, N4.yord)]

pZ = [(N1.xabs, N1.yord), (N2.xabs, N2.yord), (N3.xabs, N3.yord),
      (N4.xabs, N4.yord), (N1.xabs, N1.yord)]

pt1 = [(C1.xabs, C1.yord), (M1.xabs, M1.yord)]
pt2 = [(C1.xabs, C1.yord), (M2.xabs, M2.yord)]
pt3 = [(C1.xabs, C1.yord), (M3.xabs, M3.yord)]
pt4 = [(C1.xabs, C1.yord), (M4.xabs, M4.yord)]

pt = [(M1.xabs, M1.yord), (M2.xabs, M2.yord), (M3.xabs, M3.yord),
      (M4.xabs, M4.yord), (M1.xabs, M1.yord)]

fig, ax = plt.subplots()
fig.canvas.draw()
ax.set_aspect(1)
ax.scatter(M_X, M_Y)
ax.scatter(N_X, N_Y, color='red')
ax.plot(C1.xabs, C1.yord, marker='+')
ax.annotate('C', (C1.xabs, C1.yord+0.1))
ax.plot(*zip(*pZ), color='green')
ax.plot(*zip(*p1), *zip(*p2), *zip(*p3), *zip(*p4), color='green')
ax.plot(*zip(*pt), ls='--', color='orange')
ax.plot(*zip(*pt1), *zip(*pt2), *zip(*pt3), *zip(*pt4), ls='--',
        color='orange')
plt.xlim((-6, 7))
plt.ylim((-6, 6))
ax.grid('True')
plt.title(f'Homothétie de rapport {L} et '
          + f'de centre C({C1.xabs}, {C1.yord})')
plt.savefig('homothetie.png')
plt.close('all')
