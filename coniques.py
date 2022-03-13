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
def Trace_Parabole(p, y, frac = 0.1):
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
    ax.set_ylim([y[0], -y[0]])
    ax.set_xlim([y[0]+2, -y[0]])  
    ax.set_aspect('equal', adjustable='box')
    ax.plot(x,y)
    ax.plot(xd, y)
    ax.plot(K.x, K.y, '+')
    ax.plot(F.x, F.y, '+')
    ax.plot(M.x, M.y, 'x')
    ax.plot(H.x, H.y, 'x')
    ax.annotate('K', (K.x, K.y))
    ax.annotate('F', (F.x, F.y))
    ax.annotate('D', (K.x, y2*0.8))
    ax.annotate('M', (M.x, M.y*1.1))
    ax.annotate('H', (H.x, H.y))
    ax.plot(*zip(*MH), *zip(*MF), ls='--')
    #plt.axis('off')
    plt.grid(False)
    #plt.title(f"Tracé d'une parabole, $MF = e MH$, avec $p = {p}$")       
    plt.grid(True)
    plt.savefig(f"Tracé_parabole_p={p}.png", format='png')
    plt.close('all')
#
# y1 = -4
# y2 = -y1
# Nb = 1000
#
# y = np.linspace(y1, y2, Nb)
# for p in (0.5, 0.75, 1, 1.5, 1.75, 2, 2.5, 3):
#     Trace_Parabole(p, y, frac = 0.3)
#%% Partie hyperbole e>1
#L’hyperbole H est la réunion des deux courbes paramétrées suivantes :
#Γ1 : x(t) = a cosh(t), y(t) = b sinh(t)
#Γ2 : x(t) = −a cosh(t), y(t) = b sinh(t)   

def Trace_Hyperbole(p, e, t, frac=0.422, fact=1.2):
    a = p/(e**2-1)
    b = p/(np.sqrt(e**2-1))
    #c = np.sqrt(a**2+b**2)
    c = p*e/(e**2-1)
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
    #On définit les asymptotes
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
    lim = np.ceil(c)*fact
    ax.set_ylim([-lim, lim])
    ax.set_xlim([-lim, lim])  
    ax.set_aspect('equal', adjustable='box')
    ax.plot(x1H,y1H, x2H,y2H, color='blue')
    ax.plot(xAs,y1As, -xAs,y2As, color='black')
    ax.plot(x1d, t, color = 'red')    
    ax.plot(K.x, K.y, F1.x, F1.y,F2.x, F2.y,A1.x, A1.y,A2.x, A2.y, O.x, O.y,
            marker='+', color='black')
    ax.plot(M.x, M.y, H.x, H.y, marker='x', color='black')
    ax.annotate('O', (O.x, O.y))
    ax.annotate('A1', (A1.x*0.9, A1.y))
    ax.annotate('A2', (A2.x*0.77, A2.y*1.1))    
    ax.annotate('K', (K.x*0.8, K.y))
    ax.annotate('F1', (F1.x*1.1, F1.y))
    ax.annotate('F2', (F2.x*0.9, F2.y))
    ax.annotate('D', (K.x*0.8, -H.y*1.1))
    ax.annotate('M', (M.x*1.1, M.y))
    ax.annotate('H', (H.x*0.8, H.y))
    ax.plot(*zip(*MH), *zip(*MF2), ls='--', color='green')
    #plt.axis('off')
    plt.grid(False)
    e1 = np.round(e, 2)
    plt.title(f"Tracé d'une parabole, $MF = e MH$, avec $p = {p}$ et $e = {e1}$")       
    plt.grid(True)
    plt.savefig(f"Tracé_hyperbole_e={e1}_p={p}.png", format='png')
    plt.close('all')
    
#Fonctionne
t = np.linspace(-5, 5, 1000) 
Trace_Hyperbole(3, 1.5, t)   
Trace_Hyperbole(1/2, np.sqrt(5/4), t)
Trace_Hyperbole(1, 1.5, t)
Trace_Hyperbole(1, 1.732, t)