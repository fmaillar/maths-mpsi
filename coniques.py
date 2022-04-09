# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 23:50:00 2022

@author: e_fmaill
"""
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import numpy as np
import math

NewGreen  = '#2ca02c'
NewBlue   = '#1f77b4'
NewOrange = '#ff7f0e'

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.coords = (x, y)        
    def affichage(self):
        return '('+str(self.x)+';'+str(self.y)+')'

    def milieu(self,p):
        return Point((self.x+p.x)/2,(self.y+p.y)/2)

    def vecteur(self,p):
        return Vecteur(p.x-self.x,p.y-self.y)

    def distance(self,p):
        return self.vecteur(p).norme()
    
    def coord(self):
        return (self.x, self.y)
    
class Vecteur:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def coord(self):
        return (self.x, self.y)

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

#%% Partie parabole e = 1
def Trace_Parabole(p, y, label, frac = 0.1):
    y2 = max(y)
    Nb = len(y)
    #On definit le foyer
    F = Point(p/2, 0)
    #
    Ni = int(Nb*frac)
    #On définit la directrice
    xd = -p/2*np.ones(Nb)
    # On définit la conique    
    x = (1/(2*p))*y**2    
    # On définit les points caractéristiques
    M = Point(x[Ni], y[Ni])
    H = Point(xd[Ni], y[Ni])
    K = Point(H.x, 0)
    # On définit les segments
    #Segment MH
    MH = [M.coord(), H.coord()]
    #Segment MF
    MF = [M.coord(), F.coord()]
    # On trace
    fig, ax = plt.subplots()
    ax.set_ylim([-3, 3])
    ax.set_xlim([-2, 5])  
    ax.set_aspect('equal', adjustable='box')
    ax.plot(x,y)
    ax.plot(xd, y)
    ax.plot(K.x, K.y, F.x, F.y, M.x, M.y, H.x, H.y, 
            marker = '+', color = 'black')
    ax.annotate('$K$', (K.x, K.y))
    ax.annotate('$F$', (F.x, F.y))
    ax.annotate('$D$', (K.x, y2*0.8))
    ax.annotate('$M$', (M.x, M.y*1.1))
    ax.annotate('$H$', (H.x, H.y))
    ax.plot(*zip(*MH), *zip(*MF), ls='--', color=NewGreen)
    #plt.axis('off')
    plt.grid(False)
    plt.title(f"$MF = e MH$, avec $p = {p:.2f}$ et $e = 1$")       
    plt.grid(True)
    plt.savefig("Tracé_parabole_"+label+".png", format='png')
    plt.close('all')
#
y1 = -4
y2 = -y1
Nb = 1000

y = np.linspace(y1, y2, Nb)
for p in (0.5, 0.75, 1, 1.5, 1.75, 2, 2.5, 3):
    Trace_Parabole(p, y, str(p), frac = 0.39)

#%% Partie hyperbole e>1
#L’hyperbole H est la réunion des deux courbes paramétrées suivantes :
#Γ1 : x(t) = a cosh(t), y(t) = b sinh(t)
#Γ2 : x(t) = −a cosh(t), y(t) = b sinh(t)   

def Trace_Hyperbole(a, b, t, label, frac=0.422, fact=1.2,):
#    a = p/(e**2-1)
#    b = p/(np.sqrt(e**2-1))
    c = np.sqrt(a**2+b**2)
#    c = p*e/(e**2-1)
    e = np.sqrt(1+(b/a)**2)
    p = b**2/a
    Nb = len(t)
    Ni = int(Nb*frac)
    #On definit les foyers
    F1 = Point(-c, 0)
    F2 = Point(c, 0)
    #On definit les sommets
    A1 = Point(-a, 0)
    A2 = Point(a, 0)
    #On definit le centre
    O = Point(0,0)
    #On définit les asymptote
    xAs = t
    y1As = b/a * xAs
    y2As = b/a * xAs
    #On définit les directrices
    x1d = a**2/c*np.ones(Nb)
#    x2d = -a**2/c*np.ones(Nb)
    #On définit l'hyperbole
    x1H = a*np.cosh(t)
    y1H = b*np.sinh(t)
    x2H = -a*np.cosh(t)
    y2H = b*np.sinh(t)
    # On définit les points caractéristiques
    M = Point(x1H[Ni], y1H[Ni])
    H = Point(x1d[Ni], y1H[Ni])
    K = Point(H.x, 0)
    # On définit les segments
    #Segment MH
    MH = [M.coord(), H.coord()]
    #Segment MF
    MF2 = [M.coord(), F2.coord()]
    # On trace
    fig, ax = plt.subplots()
    lim = 3#np.ceil(c)*fact
    ax.set_ylim([-lim, lim])
    ax.set_xlim([-lim, lim])  
    ax.set_aspect('equal', adjustable='box')
    ax.plot(x1H,y1H, x2H,y2H, color=NewBlue)
    ax.plot(xAs,y1As, -xAs,y2As, ls = '--', color='black')
    ax.plot(x1d, t, color = NewOrange)    
    ax.plot(K.x, K.y, F1.x, F1.y,F2.x, F2.y,A1.x, A1.y,A2.x, A2.y, O.x, O.y,
            marker='+', color='black')
    ax.plot(M.x, M.y, H.x, H.y, marker='x', color='black')
    ax.annotate('$O$', (O.x, O.y))
    ax.annotate('$A_1$', (A1.x*0.9, A1.y))
    ax.annotate('$A_2$', (A2.x*0.77, A2.y*1.1))    
    ax.annotate('$K$', (K.x*0.8, K.y))
    ax.annotate('$F_1$', (F1.x*1.1, F1.y))
    ax.annotate('$F_2$', (F2.x*0.9, F2.y))
    ax.annotate('$D$', (K.x*0.8, -H.y*1.1))
    ax.annotate('$M$', (M.x*1.1, M.y))
    ax.annotate('$H$', (H.x*0.8, H.y))
    ax.plot(*zip(*MH), *zip(*MF2), ls='--', color=NewGreen)
    #plt.axis('off')
    plt.grid(False)
#    e1 = np.round(e, 2)
    plt.title(f"$MF_2 = e MH$, avec $p = {p:.2f}$ et $e = {e:.2f}$")       
    plt.grid(True)
    plt.savefig("Tracé_hyperbole_"+label+".png", format='png')
    plt.close('all')
    
#Fonctionne
t = np.linspace(-5, 5, 1000) 

Trace_Hyperbole(1, np.sqrt(1/3), t, label="1")
Trace_Hyperbole(1, np.sqrt(1/2), t, label="2")   
Trace_Hyperbole(1, 1, t, label="3")   
Trace_Hyperbole(1, np.sqrt(2), t, label="4")
Trace_Hyperbole(1, np.sqrt(3), t, label="5")
Trace_Hyperbole(1, np.sqrt(5), t, label="6")

#%% Partie ellipse

def Trace_Ellipse(a, b, t, label, frac=0.422, fact=1):
    c = np.sqrt(a**2 - b**2)
    e = c/a
#    d = b**2/c
    p = b**2/a
    Nb = len(t)
    Ni = int(Nb*frac)
    #On definit les foyers
    F1 = Point(-c, 0)
    F2 = Point(c, 0)
    #On definit le centre
    O = Point(0,0)
    x1d = a**2/c*np.ones(Nb)
#    x2d = -a**2/c*np.ones(Nb)
    #On définit l'ellipse
    x1E = a*np.cos(t)
    y1E = b*np.sin(t)
    # On définit les points caractéristiques
    M = Point(x1E[Ni], y1E[Ni])
    H = Point(x1d[Ni], y1E[Ni])
    K = Point(H.x, 0)
    # On définit les segments
    #Segment MH
    MH = [M.coord(), H.coord()]
    #Segment MF
    MF2 = [M.coord(), F2.coord()]
    # On trace
    fig, ax = plt.subplots()
    #lim = np.ceil(c)*fact
    ax.set_ylim([-5, 5])
    ax.set_xlim([-5, 5])  
    ax.set_aspect('equal', adjustable='box')
    # Trace en bleu
    ax.plot(x1E, y1E, color = NewBlue)
    # trace en orange
    ax.plot(x1d, t, color = NewOrange)    
    ax.plot(K.x, K.y, F1.x, F1.y,F2.x, F2.y, O.x, O.y,
            marker='+', color='black')
    ax.plot(M.x, M.y, H.x, H.y, marker='x', color='black')
    ax.annotate('$O$', (O.x, O.y))
    ax.annotate('$K$', (K.x*1.2, K.y))
    ax.annotate('$F_1$', (F1.x*1.1, F1.y))
    ax.annotate('$F_2$', (F2.x*0.9, F2.y))
    ax.annotate('$D$', (K.x*1.2, -H.y*1.1))
    ax.annotate('$M$', (M.x*1.1, M.y))
    ax.annotate('$H$', (H.x*1.2, H.y))
    # Trace en vert
    ax.plot(*zip(*MH), *zip(*MF2), ls='--', color=NewGreen) 
    #plt.axis('off')
    plt.grid(False)
    e1 = np.round(e, 2)
    plt.title(f"$MF_2 = e MH$, avec $p = {p:.2f}$ et $e = {e1:.2f}$")       
    plt.grid(True)
    plt.savefig("Tracé_ellipse_"+label+".png", format='png')
    plt.close('all')

t = np.linspace(-5, 5, 1000) 
"""Rappel
c = np.sqrt(a**2 - b**2)
e = c/a
d = b**2/c
p = b**2/a
"""
Trace_Ellipse(1.5, 1, t, frac=0.33, fact = 1.5, label="1")   
Trace_Ellipse(2, 1, t, frac=0.33, fact = 1.5, label="2")   
Trace_Ellipse(2.5, 1, t, frac=0.33, fact = 1.5, label="3")
Trace_Ellipse(3, 1, t, frac=0.33, fact = 1.5, label="4")
Trace_Ellipse(3.5, 1, t, frac=0.33, fact = 1.5, label="5")
Trace_Ellipse(4, 1, t, frac=0.33, fact = 1.5, label="6")

#%% Tracé des tangentes

def Equation_parabole(p, t):
    y = t
    x = t**2/(2*p)
    return np.array((x, y))

def Equation_hyperbole(a, b, t):
    y  = b  * np.sinh(t)
    x1 = -a * np.cosh(t)
    x2 = a  * np.cosh(t)
    Z1 = np.array((x1,y))
    Z2 = np.array((x2,y))
    Z  = np.concatenate((Z1, Z2), axis=0)
    return Z

def Equation_ellipse(a, b, t):
    y = b * np.sin(t)
    x = a * np.cos(t)
    return np.array((x, y))

def Equation_tangente(M, x, genre, a=1, b=1, p = 1):    
    if genre=="hyperbole":        
            n = 1
            return (-1)**n*b**2/M.y*(1-x*M.x/a**2)
    elif genre=="ellipse":
            n = 0
            return (-1)**n*b**2/M.y*(1-x*M.x/a**2)
    elif genre=="parabole":
            return 1/M.y*p*(x+M.x)
    else :
            raise NameError("Ce type de conique n'existe pas")

def Foyer(genre, a, b):
    if genre=="hyperbole":
        c = np.sqrt(a**2+b**2)
    elif genre=="ellipse":
        c = np.sqrt(a**2-b**2)        
    F1 = Point(-c, 0)
    F2 = Point(c, 0)
    return F1, F2
        

N = 10000
p = 1
a = 1.2
b = 1

t = np.linspace(-10,10,N)
x = np.linspace(-3, 3, 20)
P = Equation_parabole(p, t)
H = Equation_hyperbole(b, a, t)
E = Equation_ellipse(a, b, t)
##########
i1 = 4450 #np.rint(N*0.3)
i2 = 5150 #np.rint(N*0.8)
M1 = Point(H[0,i1], H[1,i1])
y1 = Equation_tangente(M1, x, 'hyperbole', a=b, b=a)
M2 = Point(H[2,i2], H[3,i2])
y2 = Equation_tangente(M2, x, 'hyperbole', a=b, b=a)
F1, F2 = Foyer('hyperbole', a, b)
M1F1 = [M1.coord(), F1.coord()]
M1F2 = [M1.coord(), F2.coord()]
M2F1 = [M2.coord(), F1.coord()]
M2F2 = [M2.coord(), F2.coord()]

###########
M3 = Point(E[0,i1], E[1,i1])
y3 = Equation_tangente(M3, x, 'ellipse', a=a, b=b)
M4 = Point(E[0,i2], E[1,i2])
y4 = Equation_tangente(M4, x, 'ellipse', a=a, b=b)
F3, F4 = Foyer('ellipse', a, b)
M3F3 = [M3.coord(), F3.coord()]
M3F4 = [M3.coord(), F4.coord()]
M4F3 = [M4.coord(), F3.coord()]
M4F4 = [M4.coord(), F4.coord()]

###########
i3 = 4350
i4 = 5450
M5 = Point(P[0,i3], P[1,i3])
y5 = Equation_tangente(M5, x, 'parabole', p=p)
M6 = Point(P[0,i4], P[1,i4])
y6 = Equation_tangente(M6, x, 'parabole', p=p)
F  = Point(p/2, 0)

xd = -p/2*np.ones(N)
#M = Point(x[Ni], y[Ni])
H5 = Point(xd[i3], P[1,i3])
H6 = Point(xd[i4], P[1,i4])
K5 = Point(H5.x, 0)
K6 = Point(H6.x, 0)
# On définit les segments
#Segment MH
M5H5 = [M5.coord(), H5.coord()]
M6H6 = [M6.coord(), H6.coord()]
#Segment MF
M5F = [M5.coord(), F.coord()]
M6F = [M6.coord(), F.coord()]
#Segment FH
FH5 = [F.coord(), H5.coord()]
FH6 = [F.coord(), H6.coord()]


###########
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(H[0,:], H[1, :],
         H[2,:], H[3, :],
        color = NewGreen)
plt.plot(M1.x, M1.y, marker = '+', color = 'black') 
plt.plot(M2.x, M2.y, marker = '+', color = 'black')
plt.plot(F1.x, F1.y, marker = '+', color = 'black') 
plt.plot(F2.x, F2.y, marker = '+', color = 'black')
ax.plot(*zip(*M1F1), *zip(*M1F2), ls='--', color=NewBlue)
ax.plot(*zip(*M2F1), *zip(*M2F2), ls='--', color=NewOrange)
ax.annotate('$M_1$', M1.coords)
ax.annotate('$M_2$', M2.coords)
ax.annotate('$F_1$', F1.coords)
ax.annotate('$F_2$', F2.coords)
plt.xlim([-2.5,2.5])
plt.ylim([-2.5,2.5])
plt.grid(True)
plt.savefig('Tangente_hyperbole.png', format='png')
plt.close(fig)

fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
plt.plot(x, y3)
plt.plot(x, y4)
plt.plot(E[0,:], E[1, :])
plt.plot(M3.x, M3.y, marker = '+', color = 'black') 
plt.plot(M4.x, M4.y, marker = '+', color = 'black')
plt.plot(F3.x, F3.y, marker = '+', color = 'black') 
plt.plot(F4.x, F4.y, marker = '+', color = 'black')
ax.plot(*zip(*M3F3), *zip(*M3F4), ls='--', color=NewBlue)
ax.plot(*zip(*M4F3), *zip(*M4F4), ls='--', color=NewOrange)
ax.annotate('$M_3$', M3.coords)
ax.annotate('$M_4$', M4.coords)
ax.annotate('$F_3$', F3.coords)
ax.annotate('$F_4$', F4.coords)
plt.xlim([-2.5,2.5])
plt.ylim([-2.5,2.5])
plt.grid(True)
plt.savefig('Tangente_ellipse.png', format='png')
plt.close(fig)

fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
plt.plot(x, y5)
plt.plot(x, y6)
plt.plot(xd, t, color='black')
plt.plot(P[0,:], P[1, :])
plt.plot(M5.x, M5.y, marker = '+', color = 'black')
plt.plot(M6.x, M6.y, marker = '+', color = 'black')
plt.plot(F.x, F.y, marker = '+', color = 'black')
ax.plot(*zip(*FH5), ls='--', color=NewBlue)
ax.plot(*zip(*FH6), ls='--', color=NewOrange)
ax.annotate('$M_5$', M5.coords)
ax.annotate('$M_6$', M6.coords)
ax.annotate('$F$', F.coords)
ax.annotate('$H_5$', H5.coords)
ax.annotate('$H_6$', H6.coords)
plt.xlim([-2.5,2.5])
plt.ylim([-2.5,2.5])
plt.grid(True)
plt.savefig('Tangente_parabole.png', format='png')
plt.close(fig)

plt.close('all')
