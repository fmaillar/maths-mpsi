# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 18:43:36 2022

@author: e_fmaill
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
x = [2, 4, 6]
y = [4, 3, 5]
xplotmin = 0 if min(x) > 0 else min(x)-1
yplotmin = 0 if min(y) > 0 else min(y)-1
xplotmax = 0 if max(x) < 0 else max(x)+1
yplotmax = 0 if max(y) < 0 else max(y)+1
N = len(x)
titre = ''
for i in range(N):
    titre += f'$M_{i+1} = ({x[i]},{y[i]})$ '

fig, ax = plt.subplots(1)
ax.set_aspect(1)
ax.plot(x, y, 'b', ls='', marker='.')
[plt.annotate(f'$M_{i+1}$', (x[i], y[i]), fontsize=13) for i in range(N)]
ax.arrow(1, 1, 0, 1, head_width=0.1, head_length=0.1)
plt.annotate("$\overrightarrow{i}$", (1, 2), fontsize=13)
ax.arrow(1, 1, 1, 0, head_width=0.1, head_length=0.1)
plt.annotate("$\overrightarrow{j}$", (2, 1), fontsize=13)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_title('Coordonnées cartésiennes des points '+titre)
ax.axis([xplotmin, xplotmax, yplotmin, yplotmax])

plt.grid(which='both')
# fig.show()
plt.tight_layout()
plt.savefig('CoordCartPlan', dpi=160)
