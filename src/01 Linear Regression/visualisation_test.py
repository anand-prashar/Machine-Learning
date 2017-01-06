'''
Created on Jan 4, 2017

@author: anand
'''
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 100
#===============================================================================
# for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
#     xs = randrange(n, 23, 32)
#     ys = randrange(n, 0, 100)
#     zs = randrange(n, zl, zh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)
#===============================================================================
f = open('linreg.txt')
xs1 =[]
xs2 = []
xs3 = [] 
py = []
theta = [0.025421601093201542, 1.0770710864982476, 3.9798383402188637]

for row in f:
    xs,ys,zs  = row.split(',')
    xs1.append(float(xs))
    xs2.append(float(ys))
    xs3.append(float(zs))
    
    py.append( theta[0]+xs1[-1]*theta[1]+xs2[-1]*theta[2])
ax.scatter(xs1, xs2, xs3, c='r', marker='o')
ax.scatter(xs1, xs2, py, c='b', marker='o')



ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()