# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 14:07:59 2022

@author: e_fmaill
"""
import numpy as np
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

# create data of complex numbers
data = [1-2j, -1-4j, 4+3j, -4, 2-1j, 3+9j, -2+6j, 5]
annotations = ["1-2i", "-1-4i","4+3i", "-4", "2-1i", "3+9i", "-2+6i", "5"]
# extract real part
x = [ele.real for ele in data]
# extract imaginary part
y = [ele.imag for ele in data]
  
# plot the complex numbers
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.set_aspect('equal', adjustable='box')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.scatter(x, y)
plt.ylabel('Imaginaire')
plt.xlabel('Reel')

for i, label in enumerate(annotations):
    ax.annotate(label, (x[i], y[i]))
plt.savefig('complexes.png')
plt.close()

# create data of complex numbers
data = [1+2j, 1-2j, -4+3j, -4-3j]
annotations = [r'$z_1$', r'$\bar{z_1}$', r'$z_2$', r'$\bar{z_2}$']
# extract real part
x = [ele.real for ele in data]
# extract imaginary part
y = [ele.imag for ele in data]
# plot the complex numbers
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.set_aspect('equal', adjustable='box')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.scatter(x, y)
plt.ylabel('$\Im(z)$')
plt.xlabel('$\Re(z)$')
for i, label in enumerate(annotations):
    ax.annotate(label, (x[i], y[i]))
plt.savefig('conjugue.png')
plt.close()



