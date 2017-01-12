'''
Created on Jan 4, 2017

@author: anand
'''
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



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
f = open('classification.txt')
xs1_1 =[] #class 1
xs2_1 = []
xs3_1 = [] 
xs1_2 =[] #for class 2
xs2_2 = []
xs3_2 = [] 
py = []

# theta below is by linear regression logic: [ 0.51424497 -0.01920371 -0.0180336 ]

theta = [-3.67899368 ,-1.76456966, -0.96413476, -1.04172039]
#from myself:[-3.67899368 -1.76456966 -0.96413476 -1.04172039]
#from vijay:[-0.48057089,  0.37259315  ,0.35935017  ,0.37859825]
#from Linear:[ 0.51424497,-0.01920371, -0.0180336 ]

for row in f:
    xs,ys,zs,garbage,classLabel  = row.split(',')
    if int(classLabel) == +1:
        xs1_1.append(float(xs))
        xs2_1.append(float(ys))
        xs3_1.append(float(zs))
    else:
        xs1_2.append(float(xs))
        xs2_2.append(float(ys))
        xs3_2.append(float(zs))            
    
    #py.append( theta[0]+xs1[-1]*theta[1]+xs2[-1]*theta[2]+xs3[-1]*theta[3])
ax.scatter(xs1_1, xs2_1, xs3_1, c='r', marker='o')
ax.scatter(xs1_2, xs2_2, xs3_2, c='b', marker='o')



ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()