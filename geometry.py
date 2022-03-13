# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 22:30:36 2022

@author: e_fmaill
"""

import math
import matplotlib.pyplot as plt

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def affichage(self):
        return '('+str(self.x)+';'+str(self.y)+')'

    def milieu(self,p):
        return Point((self.x+p.x)/2,(self.y+p.y)/2)

    def vecteur(self,p):
        return Vecteur(p.x-self.x,p.y-self.y)

    def distance(self,p):
        return self.vecteur(p).norme()

class Vecteur:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def affichage(self):
        return '('+str(self.x)+';'+str(self.y)+')'

    def norme(self):
        return math.hypot(self.x,self.y)

    def __add__(self,v):
        return Vecteur(self.x+v.x,self.y+v.y)

    def __rmul__(self,r):
        return Vecteur(self.x*r,self.y*r)

    def __mul__(self,v):
        return self.x*v.x+self.y*v.y

    def colin(self,v):
        return self.x*v.y==self.y*v.x

    def ortho(self,v):
        return self*v==0


class Droite:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def directeur(self):
        return self.a.vecteur(self.b)

    def normal(self):
        return Vecteur(-self.directeur().y,self.directeur().x)

    def cartesienne(self):
        return '('+str(self.normal().x)+')x+('+str(self.normal().y)+')y='+str(self.normal().x*self.a.x+self.normal().y*self.a.y)

    def cd(self):
        return self.directeur().y/self.directeur().x

    def oalo(self):
        return self.a.y-self.cd()*self.a.x

    def reduite(self):
        return 'y='+str(self.cd())+'x+('+str(self.oalo())+')'

    def parallele(self,d):
        return self.directeur().colin(d.directeur())

    def perpendiculaire(self,d):
        return self.normal().ortho(d.normal())

a=Point(-1,3.0)
b=Point(5,1)
c=Point(1,5)

u=c.vecteur(a)
v=c.vecteur(b)

print(u*v)
print(u.ortho(v))

d1=Droite(c,a)
d2=Droite(c,b)

print(d1.perpendiculaire(d2))

def Homothety(mu, S, M):
    Temp = Vecteur(M.x-S.x, M.y-S.y)
    Outx = S.x + mu*Temp.x
    Outy = S.y + mu*Temp.y
    return Point(Outx, Outy)
    
C = Point(-4,0)
L = 2
M1 = Point(-1,2)
M2 = Point(1,2)
M3 = Point(1,-2)
M4 = Point(-1,-2)

N1 = Homothety(L, C, M1)
N2 = Homothety(L, C, M2)
N3 = Homothety(L, C, M3)
N4 = Homothety(L, C, M4)

M_X = [M1.x, M2.x, M3.x, M4.x]
M_Y = [M1.y, M2.y, M3.y, M4.y]
N_X = [N1.x, N2.x, N3.x, N4.x]
N_Y = [N1.y, N2.y, N3.y, N4.y]


p1 = [(M1.x, M1.y), (N1.x, N1.y)]
p2 = [(M2.x, M2.y), (N2.x, N2.y)]
p3 = [(M3.x, M3.y), (N3.x, N3.y)]
p4 = [(M4.x, M4.y), (N4.x, N4.y)]

p = [(N1.x, N1.y), (N2.x, N2.y), (N3.x, N3.y), (N4.x, N4.y), (N1.x, N1.y)]

pt1 = [(C.x, C.y), (M1.x, M1.y)]
pt2 = [(C.x, C.y), (M2.x, M2.y)]
pt3 = [(C.x, C.y), (M3.x, M3.y)]
pt4 = [(C.x, C.y), (M4.x, M4.y)]

pt = [(M1.x, M1.y), (M2.x, M2.y), (M3.x, M3.y), (M4.x, M4.y), (M1.x, M1.y)]

fig, ax = plt.subplots()
fig.canvas.draw()
ax.set_aspect(1)
ax.scatter(M_X, M_Y)
ax.scatter(N_X, N_Y, color = 'red')
ax.plot(C.x, C.y, marker='+')
ax.annotate('C', (C.x, C.y+0.1))
ax.plot(*zip(*p), color = 'green')
ax.plot(*zip(*p1), *zip(*p2), *zip(*p3), *zip(*p4), color = 'green')
ax.plot(*zip(*pt), ls='--', color = 'orange')
ax.plot(*zip(*pt1),*zip(*pt2), *zip(*pt3), *zip(*pt4), ls='--', color = 'orange')
plt.xlim((-6,7))
plt.ylim((-6,6))
ax.grid('True')
plt.title("Homothétie de rapport {l} et de centre C({x}, {y})".format(l=L, x=C.x, y=C.y))
plt.savefig('homothetie.png')