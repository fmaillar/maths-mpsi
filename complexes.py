# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 14:07:59 2022

@author: e_fmaill
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['text.usetex'] = True


# create data of complex numbers
data = [1-2j, -1-4j, 4+3j, -4, 2-1j, 3+9j, -2+6j, 5]
annotations = [r"$z_1=1-2i$", r"$z_2=-1-4i$", r"$z_3=4+3i$", r"$z_4=-4$",
               r"$z_5=2-1i$", r"$z_6=3+9i$", r"$z_7=-2+6i$", r"$z_8=5$"]
# extract real part
x = [ele.real for ele in data]
# extract imaginary part
y = [ele.imag for ele in data]
# plot the complex numbers
fig = plt.figure()
ax = fig.add_subplot(111)
# ax.set_aspect('equal', adjustable='box')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.scatter(x, y)
plt.ylabel(r'$\Im(z)$')
plt.xlabel(r'$\Re(z)$')
for i, label in enumerate(annotations):
    ax.annotate(label, (x[i], y[i]))
plt.grid('True', which='both')
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
# ax.set_aspect('equal', adjustable='box')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.scatter(x, y)
plt.ylabel(r'$\Im(z)$')
plt.xlabel(r'$\Re(z)$')
for i, label in enumerate(annotations):
    ax.annotate(label, (x[i], y[i]))
plt.grid('True', which='both')
plt.savefig('conjugue.png')
plt.close('all')
