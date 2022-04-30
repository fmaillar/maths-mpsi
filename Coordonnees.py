# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 00:59:04 2022

@author: e_fmaill
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
# from mpl_toolkits.mplot3d import Axes3D

NewGreen = '#2ca02c'
NewBlue = '#1f77b4'
NewOrange = '#ff7f0e'

vectors = np.array([[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 1]])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for vector in vectors:
    v = np.array([vector[3], vector[4], vector[5]])
    vlength = np.linalg.norm(v)
    ax.quiver(vector[0], vector[1], vector[2], vector[3], vector[4], vector[5],
              pivot='tail', length=vlength, arrow_length_ratio=0.3/vlength)
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
e = 1/5
ax.text(0-e, 0-e, 0-e, '$O$')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# plt.show()
plt.savefig("coord-cartesiennes", dpi=120)

r = 1
theta = np.pi/5
x = r*np.cos(theta)
y = r*np.sin(theta)
z = 0.1

OM = [(0, 0, 0), (x, y, z)]

repcart = np.array([[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 1]])
vectors = np.array([[x, y, z, x/r, y/r, 0], [x, y, z, -y/r, x/r, 0],
                    [x, y, z, 0, 0, z/z]])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.view_init(elev=40., azim=75.)
for vector in vectors:
    v = np.array([vector[3], vector[4], vector[5]])
    vlength = np.linalg.norm(v)
    ax.quiver(vector[0], vector[1], vector[2], vector[3], vector[4], vector[5],
              pivot='tail', length=vlength, arrow_length_ratio=0.3/vlength,
              color=NewOrange)
for vector in repcart:
    v = np.array([vector[3], vector[4], vector[5]])
    vlength = np.linalg.norm(v)
    ax.quiver(vector[0], vector[1], vector[2], vector[3], vector[4], vector[5],
              pivot='tail', length=vlength, arrow_length_ratio=0.3/vlength)
ax.plot(*zip(*OM), ls='--', color=NewBlue)
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
e = 0.02
ax.text(x-e, y-e, z-e, "$M$")
ax.text(-e, -e, -e, "$O$")
ax.text(0.1, -0.1, 0, "$\\theta$")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# plt.show()
plt.tight_layout()
plt.savefig("coord-cylindriques", dpi=120)

r = 1
theta = np.pi/6
phi = np.pi/5
x = r*np.sin(theta)*np.cos(phi)
y = r*np.sin(theta)*np.sin(phi)
z = r*np.cos(theta)

OM = [(0, 0, 0), (x, y, z)]

repcart = np.array([[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 1]])
vectors = np.array([[x, y, z, np.sin(theta) * np.cos(phi),
                   np.sin(theta)*np.sin(phi), np.cos(theta)],
                   [x, y, z, np.cos(theta)*np.cos(phi),
                   np.cos(theta)*np.sin(phi), -np.sin(theta)],
                   [x, y, z, -np.sin(phi), np.cos(phi), 0]])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.view_init(elev=29., azim=70.)
for vector in vectors:
    v = np.array([vector[3], vector[4], vector[5]])
    vlength = np.linalg.norm(v)
    ax.quiver(vector[0], vector[1], vector[2], vector[3], vector[4], vector[5],
              pivot='tail', length=vlength, arrow_length_ratio=0.3/vlength,
              color=NewOrange)

for vector in repcart:
    v = np.array([vector[3], vector[4], vector[5]])
    vlength = np.linalg.norm(v)
    ax.quiver(vector[0], vector[1], vector[2], vector[3], vector[4], vector[5],
              pivot='tail', length=vlength, arrow_length_ratio=0.3/vlength)
ax.plot(*zip(*OM), ls='--', color=NewBlue)
ax.set_xlim([-0.5, 2])
ax.set_ylim([-0.5, 2])
ax.set_zlim([-0.5, 2])
e = 0.02
ax.text(x-e, y-e, z-e, "$M$")
ax.text(-e, -e, -e, "$O$")
# ax.text(0.1, -0.1, 0, "$\\theta$")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# plt.show()
plt.tight_layout()
plt.savefig("coord-spheriques", dpi=120)
