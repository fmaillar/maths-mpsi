# -*- coding: utf-8 -*-

"""
Created on Sat Mar 12 22:30:36 2022

@author: e_fmaill
"""

import math


class Point:
    """The class Point defines a point."""

    def __init__(self, xabs, yord):
        self.xabs = xabs
        self.yord = yord

    def coord(self):
        """Permet de definir les coordonnées."""
        return (self.xabs, self.yord)

    # def str_coord(self):
    #     """Renvoie une STR avec les coord."""
    #     return str(self.xabs)

    def affichage(self):
        """Permet d'afficher le point."""
        return '('+str(self.xabs)+';'+str(self.yord)+')'

    def milieu(self, point):
        """Defini le milieu de deux points."""
        return Point((self.xabs+point.xabs)/2, (self.yord+point.yord)/2)

    def vecteur(self, point):
        """Renvoie le vecteur directeur entre deux points."""
        return Vecteur(point.xabs-self.xabs, point.yord-self.yord)

    def distance(self, point):
        """Renvoie la distance entre deux points."""
        return self.vecteur(point).norme()


class Vecteur:
    """Cette classe défini un vecteur."""

    def __init__(self, xabs, yord):
        self.xabs = xabs
        self.yord = yord

    def affichage(self):
        """Idem que pour la classe Point."""
        return '('+str(self.xabs)+';'+str(self.yord)+')'

    def norme(self):
        """Renvoie la norme d'un vecteur."""
        return math.hypot(self.xabs, self.yord)

    def __add__(self, vec):
        """C'est l'addition de vecteurs."""
        return Vecteur(self.xabs+vec.xabs, self.yord+vec.yord)

    def __rmul__(self, facteur):
        """C'est la multiplication par un scalaire."""
        return Vecteur(self.xabs*facteur, self.yord*facteur)

    def __mul__(self, vec):
        """C'est la multiplication entre vecteurs."""
        return self.xabs*vec.xabs+self.yord*vec.yord

    def colin(self, vec):
        """Renvoie Vrai si deux vecteurs sont colinéaires."""
        return self.xabs*vec.yord == self.yord*vec.xabs

    def ortho(self, vec):
        """Renvoie Vrai si deux vecteurs sont orthogonaux."""
        return self*vec == 0


class Droite:
    """Cette classe définit les droites."""

    def __init__(self, a_abs, b_ord):
        self.a_abs = a_abs
        self.b_ord = b_ord

    def directeur(self):
        """Renvoie le vecteur directeur de la droite."""
        return self.a_abs.vecteur(self.b_ord)

    def normal(self):
        """Renvoie le vecteur normal de la droite."""
        return Vecteur(-self.directeur().yord, self.directeur().xabs)

    def cartesienne(self):
        """Renvoie l'équation cartésienne de la droite."""
        return '(' + str(self.normal().xabs) + ')x + (' + str(self.normal().yord) + \
            ')y = ' + str(self.normal().xabs * self.a_abs.xabs +
                          self.normal().yord * self.a_abs.yord)

    def coefdir(self):
        """Renvoie le coefficient directeur de la droite."""
        return self.directeur().yord/self.directeur().abs

    def oalo(self):
        """Renvoie l'ordonnée à l'origine de la droite."""
        return self.a_abs.yord-self.coefdir()*self.a_abs.xabs

    def reduite(self):
        """Renvoie l'équation réduite de la droite."""
        return 'y='+str(self.coefdir())+'x+('+str(self.oalo())+')'

    def parallele(self, droite):
        """Renvoie Vrai si les droites sont parallèles."""
        return self.directeur().colin(droite.directeur())

    def perpendiculaire(self, droite):
        """Renvoie Vrai si les droites sont perpendiculaires."""
        return self.normal().ortho(droite.normal())


def homothety(coeff, centre, point):
    """Cette methode definit une homot de rapport coeff et de centre Centre."""
    temp = Vecteur(point.xabs-centre.xabs, point.yord-centre.yord)
    outx = centre.xabs + coeff*temp.xabs
    outy = centre.yord + coeff*temp.yord
    return Point(outx, outy)
