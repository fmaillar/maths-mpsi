# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 23:50:00 2022

@author: e_fmaill
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
# import math
from geometry import Point

mpl.rcParams['text.usetex'] = True

NewGreen = '#2ca02c'
NewBlue = '#1f77b4'
NewOrange = '#ff7f0e'
# Partie parabole e = 1


def Trace_Parabole(p, y, label, frac=0.1):
    """Cette methode trace la parabole."""
    y2 = max(y)
    Nb = len(y)
    # On definit le foyer
    F = Point(p/2, 0)
    #
    Ni = int(Nb*frac)
    # On définit la directrice
    xd = -p/2*np.ones(Nb)
    # On définit la conique
    x = (1/(2*p))*y**2
    # On définit les points caractéristiques
    M = Point(x[Ni], y[Ni])
    H = Point(xd[Ni], y[Ni])
    K = Point(H.xabs, 0)
    # On définit les segments
    # Segment MH
    MH = [M.coord(), H.coord()]
    # Segment MF
    MF = [M.coord(), F.coord()]
    # On trace
    fig, ax = plt.subplots()
    ax.set_ylim([-3, 3])
    ax.set_xlim([-2, 5])
    ax.set_aspect('equal', adjustable='box')
    ax.plot(x, y)
    ax.plot(xd, y)
    ax.plot(K.xabs, K.yord, F.xabs, F.yord, M.xabs, M.yord, H.xabs, H.yord,
            marker='+', color='black')
    ax.annotate('$K$', (K.xabs, K.yord))
    ax.annotate('$F$', (F.xabs, F.yord))
    ax.annotate('$D$', (K.xabs, y2*0.8))
    ax.annotate('$M$', (M.xabs, M.yord*1.1))
    ax.annotate('$H$', (H.xabs, H.yord))
    ax.plot(*zip(*MH), *zip(*MF), ls='--', color=NewGreen)
    # plt.axis('off')
    plt.grid(False)
    plt.title(f"$MF = e MH$, avec $p = {p:.2f}$ et $e = 1$")
    plt.grid(True)
    plt.savefig("Tracé_parabole_"+label+".png", format='png')
    plt.close('all')


y1 = -4
y2 = -y1
Nb = 1000

y = np.linspace(y1, y2, Nb)
for p in (0.5, 0.75, 1, 1.5, 1.75, 2, 2.5, 3):
    Trace_Parabole(p, y, str(p), frac=0.39)

# Partie hyperbole e>1
# L’hyperbole H est la réunion des deux courbes paramétrées suivantes :
# Γ1 : x(t) = a cosh(t), y(t) = b sinh(t)
# Γ2 : x(t) = −a cosh(t), y(t) = b sinh(t)


def Trace_Hyperbole(a, b, t, label, frac=0.422, fact=1.2,):
    """Cette methode trace l'hyperbole."""
#    a = p/(e**2-1)
#    b = p/(np.sqrt(e**2-1))
    c = np.sqrt(a**2+b**2)
#    c = p*e/(e**2-1)
    e = np.sqrt(1+(b/a)**2)
    p = b**2/a
    Nb = len(t)
    Ni = int(Nb*frac)
    # On definit les foyers
    F1 = Point(-c, 0)
    F2 = Point(c, 0)
    # On definit les sommets
    A1 = Point(-a, 0)
    A2 = Point(a, 0)
    # On definit le centre
    Origine = Point(0, 0)
    # On définit les asymptote
    xAs = t
    y1As = b/a * xAs
    y2As = b/a * xAs
    # On définit les directrices
    x1d = a**2/c*np.ones(Nb)
    # x2d = -a**2/c*np.ones(Nb)
    # On définit l'hyperbole
    x1H = a*np.cosh(t)
    y1H = b*np.sinh(t)
    x2H = -a*np.cosh(t)
    y2H = b*np.sinh(t)
    # On définit les points caractéristiques
    M = Point(x1H[Ni], y1H[Ni])
    H = Point(x1d[Ni], y1H[Ni])
    K = Point(H.xabs, 0)
    # On définit les segments
    # Segment MH
    MH = [M.coord(), H.coord()]
    # Segment MF
    MF2 = [M.coord(), F2.coord()]
    # On trace
    fig, ax = plt.subplots()
    # lim = np.ceil(c)*fact
    lim = 3
    ax.set_ylim([-lim, lim])
    ax.set_xlim([-lim, lim])
    ax.set_aspect('equal', adjustable='box')
    ax.plot(x1H, y1H, x2H, y2H, color=NewBlue)
    ax.plot(xAs, y1As, -xAs, y2As, ls='--', color='black')
    ax.plot(x1d, t, color=NewOrange)
    ax.plot(K.xabs, K.yord, F1.xabs, F1.yord, F2.xabs, F2.yord, A1.xabs,
            A1.yord, A2.xabs, A2.yord, Origine.xabs, Origine.yord,
            marker='+', color='black')
    ax.plot(M.xabs, M.yord, H.xabs, H.yord, marker='x', color='black')
    ax.annotate('$O$', (Origine.xabs, Origine.yord))
    ax.annotate('$A_1$', (A1.xabs*0.9, A1.yord))
    ax.annotate('$A_2$', (A2.xabs*0.77, A2.yord*1.1))
    ax.annotate('$K$', (K.xabs*0.8, K.yord))
    ax.annotate('$F_1$', (F1.xabs*1.1, F1.yord))
    ax.annotate('$F_2$', (F2.xabs*0.9, F2.yord))
    ax.annotate('$D$', (K.xabs*0.8, -H.yord*1.1))
    ax.annotate('$M$', (M.xabs*1.1, M.yord))
    ax.annotate('$H$', (H.xabs*0.8, H.yord))
    ax.plot(*zip(*MH), *zip(*MF2), ls='--', color=NewGreen)
    # plt.axis('off')
    plt.grid(False)
#    e1 = np.round(e, 2)
    plt.title(f"$MF_2 = e MH$, avec $p = {p:.2f}$ et $e = {e:.2f}$")
    plt.grid(True)
    plt.savefig("Tracé_hyperbole_"+label+".png", format='png')
    plt.close('all')


# Fonctionne
t = np.linspace(-5, 5, 1000)

Trace_Hyperbole(1, np.sqrt(1/3), t, label="1")
Trace_Hyperbole(1, np.sqrt(1/2), t, label="2")
Trace_Hyperbole(1, 1, t, label="3")
Trace_Hyperbole(1, np.sqrt(2), t, label="4")
Trace_Hyperbole(1, np.sqrt(3), t, label="5")
Trace_Hyperbole(1, np.sqrt(5), t, label="6")

# Partie ellipse


def Trace_Ellipse(a, b, t, label, frac=0.422, fact=1):
    """Cette methode trace l'ellipse."""
    c = np.sqrt(a**2 - b**2)
    e = c/a
#    d = b**2/c
    p = b**2/a
    Nb = len(t)
    Ni = int(Nb*frac)
    # On definit les foyers
    F1 = Point(-c, 0)
    F2 = Point(c, 0)
    # On definit le centre
    Origine = Point(0, 0)
    x1d = a**2/c*np.ones(Nb)
    # x2d = -a**2/c*np.ones(Nb)
    # On définit l'ellipse
    x1E = a*np.cos(t)
    y1E = b*np.sin(t)
    # On définit les points caractéristiques
    M = Point(x1E[Ni], y1E[Ni])
    H = Point(x1d[Ni], y1E[Ni])
    K = Point(H.xabs, 0)
    # On définit les segments
    # Segment MH
    MH = [M.coord(), H.coord()]
    # Segment MF
    MF2 = [M.coord(), F2.coord()]
    # On trace
    fig, ax = plt.subplots()
    # lim = np.ceil(c)*fact
    ax.set_ylim([-5, 5])
    ax.set_xlim([-5, 5])
    ax.set_aspect('equal', adjustable='box')
    # Trace en bleu
    ax.plot(x1E, y1E, color=NewBlue)
    # trace en orange
    ax.plot(x1d, t, color=NewOrange)
    ax.plot(K.xabs, K.yord, F1.xabs, F1.yord, F2.xabs, F2.yord, Origine.xabs,
            Origine.yord, marker='+', color='black')
    ax.plot(M.xabs, M.yord, H.xabs, H.yord, marker='x', color='black')
    ax.annotate('$O$', (Origine.xabs, Origine.yord))
    ax.annotate('$K$', (K.xabs*1.2, K.yord))
    ax.annotate('$F_1$', (F1.xabs*1.1, F1.yord))
    ax.annotate('$F_2$', (F2.xabs*0.9, F2.yord))
    ax.annotate('$D$', (K.xabs*1.2, -H.yord*1.1))
    ax.annotate('$M$', (M.xabs*1.1, M.yord))
    ax.annotate('$H$', (H.xabs*1.2, H.yord))
    # Trace en vert
    ax.plot(*zip(*MH), *zip(*MF2), ls='--', color=NewGreen)
    # plt.axis('off')
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
Trace_Ellipse(1.5, 1, t, frac=0.33, fact=1.5, label="1")
Trace_Ellipse(2, 1, t, frac=0.33, fact=1.5, label="2")
Trace_Ellipse(2.5, 1, t, frac=0.33, fact=1.5, label="3")
Trace_Ellipse(3, 1, t, frac=0.33, fact=1.5, label="4")
Trace_Ellipse(3.5, 1, t, frac=0.33, fact=1.5, label="5")
Trace_Ellipse(4, 1, t, frac=0.33, fact=1.5, label="6")

# Tracé des tangentes


def Equation_parabole(p, t):
    """Definit lequation de la parabole."""
    y = t
    x = t**2/(2*p)
    return np.array((x, y))


def Equation_hyperbole(a, b, t):
    """Definit lequation de l'hyperbole."""
    y = b * np.sinh(t)
    x1 = -a * np.cosh(t)
    x2 = a * np.cosh(t)
    Z1 = np.array((x1, y))
    Z2 = np.array((x2, y))
    Z = np.concatenate((Z1, Z2), axis=0)
    return Z


def Equation_ellipse(a, b, t):
    """Definit lequation de l'Ellipse."""
    y = b * np.sin(t)
    x = a * np.cos(t)
    return np.array((x, y))


def Equation_tangente(M, x, genre, a=1, b=1, p=1):
    """Definit lequation de la tangente selon le genre."""
    if genre == "hyperbole":
        n = 1
        return (-1)**n*b**2/M.yord*(1-x*M.xabs/a**2)
    elif genre == "ellipse":
        n = 0
        return (-1)**n*b**2/M.yord*(1-x*M.xabs/a**2)
    elif genre == "parabole":
        return 1/M.yord*p*(x+M.xabs)
    else:
        raise NameError("Ce type de conique n'existe pas")


def Foyer(genre, a, b):
    """Definit le ou les foyers de la conique selon le genre."""
    if genre == "hyperbole":
        c = np.sqrt(a**2+b**2)
    elif genre == "ellipse":
        c = np.sqrt(a**2-b**2)
    F1 = Point(-c, 0)
    F2 = Point(c, 0)
    return F1, F2


N = 10000
p = 1
a = 1.2
b = 1

t = np.linspace(-10, 10, N)
x = np.linspace(-3, 3, 20)
P = Equation_parabole(p, t)
H = Equation_hyperbole(b, a, t)
E = Equation_ellipse(a, b, t)
##########
i1 = 4450
i2 = 5150
M1 = Point(H[0, i1], H[1, i1])
y1 = Equation_tangente(M1, x, 'hyperbole', a=b, b=a)
M2 = Point(H[2, i2], H[3, i2])
y2 = Equation_tangente(M2, x, 'hyperbole', a=b, b=a)
F1, F2 = Foyer('hyperbole', a, b)
M1F1 = [M1.coord(), F1.coord()]
M1F2 = [M1.coord(), F2.coord()]
M2F1 = [M2.coord(), F1.coord()]
M2F2 = [M2.coord(), F2.coord()]

###########
M3 = Point(E[0, i1], E[1, i1])
y3 = Equation_tangente(M3, x, 'ellipse', a=a, b=b)
M4 = Point(E[0, i2], E[1, i2])
y4 = Equation_tangente(M4, x, 'ellipse', a=a, b=b)
F3, F4 = Foyer('ellipse', a, b)
M3F3 = [M3.coord(), F3.coord()]
M3F4 = [M3.coord(), F4.coord()]
M4F3 = [M4.coord(), F3.coord()]
M4F4 = [M4.coord(), F4.coord()]

###########
i3 = 4350
i4 = 5450
M5 = Point(P[0, i3], P[1, i3])
y5 = Equation_tangente(M5, x, 'parabole', p=p)
M6 = Point(P[0, i4], P[1, i4])
y6 = Equation_tangente(M6, x, 'parabole', p=p)
F = Point(p/2, 0)

xd = -p/2*np.ones(N)
# M = Point(x[Ni], y[Ni])
H5 = Point(xd[i3], P[1, i3])
H6 = Point(xd[i4], P[1, i4])
K5 = Point(H5.xabs, 0)
K6 = Point(H6.xabs, 0)
# On définit les segments
# Segment MH
M5H5 = [M5.coord(), H5.coord()]
M6H6 = [M6.coord(), H6.coord()]
# Segment MF
M5F = [M5.coord(), F.coord()]
M6F = [M6.coord(), F.coord()]
# Segment FH
FH5 = [F.coord(), H5.coord()]
FH6 = [F.coord(), H6.coord()]


###########
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(H[0, :], H[1, :],
         H[2, :], H[3, :],
         color=NewGreen)
plt.plot(M1.xabs, M1.yord, marker='+', color='black')
plt.plot(M2.xabs, M2.yord, marker='+', color='black')
plt.plot(F1.xabs, F1.yord, marker='+', color='black')
plt.plot(F2.xabs, F2.yord, marker='+', color='black')
ax.plot(*zip(*M1F1), *zip(*M1F2), ls='--', color=NewBlue)
ax.plot(*zip(*M2F1), *zip(*M2F2), ls='--', color=NewOrange)
ax.annotate('$M_1$', M1.coord())
ax.annotate('$M_2$', M2.coord())
ax.annotate('$F_1$', F1.coord())
ax.annotate('$F_2$', F2.coord())
plt.xlim([-2.5, 2.5])
plt.ylim([-2.5, 2.5])
plt.grid(True)
plt.savefig('Tangente_hyperbole.png', format='png')
plt.close(fig)

fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
plt.plot(x, y3)
plt.plot(x, y4)
plt.plot(E[0, :], E[1, :])
plt.plot(M3.xabs, M3.yord, marker='+', color='black')
plt.plot(M4.xabs, M4.yord, marker='+', color='black')
plt.plot(F3.xabs, F3.yord, marker='+', color='black')
plt.plot(F4.xabs, F4.yord, marker='+', color='black')
ax.plot(*zip(*M3F3), *zip(*M3F4), ls='--', color=NewBlue)
ax.plot(*zip(*M4F3), *zip(*M4F4), ls='--', color=NewOrange)
ax.annotate('$M_3$', M3.coord())
ax.annotate('$M_4$', M4.coord())
ax.annotate('$F_3$', F3.coord())
ax.annotate('$F_4$', F4.coord())
plt.xlim([-2.5, 2.5])
plt.ylim([-2.5, 2.5])
plt.grid(True)
plt.savefig('Tangente_ellipse.png', format='png')
plt.close(fig)

fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
plt.plot(x, y5)
plt.plot(x, y6)
plt.plot(xd, t, color='black')
plt.plot(P[0, :], P[1, :])
plt.plot(M5.xabs, M5.yord, marker='+', color='black')
plt.plot(M6.xabs, M6.yord, marker='+', color='black')
plt.plot(F.xabs, F.yord, marker='+', color='black')
ax.plot(*zip(*FH5), ls='--', color=NewBlue)
ax.plot(*zip(*FH6), ls='--', color=NewOrange)
ax.annotate('$M_5$', M5.coord())
ax.annotate('$M_6$', M6.coord())
ax.annotate('$F$', F.coord())
ax.annotate('$H_5$', H5.coord())
ax.annotate('$H_6$', H6.coord())
plt.xlim([-2.5, 2.5])
plt.ylim([-2.5, 2.5])
plt.grid(True)
plt.savefig('Tangente_parabole.png', format='png')
plt.close(fig)

plt.close('all')
