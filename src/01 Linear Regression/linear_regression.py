'''
Created on Jan 5, 2017

@author: anand
'''
alpha = 0.1

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fileData = np.genfromtxt('linreg.txt', delimiter = ',')

X = fileData[:,0:2]
y = fileData[:,2]
m = np.size(X)

[meanx1, meanx2] = np.mean(X,1) #col1
[meany1] = np.mean(y,1)
X[:,0] = (X[:,0]-meanx1)/m
X[:,1] = (X[:,1]-meanx2)/m
y[:,0] = (X[:,0]-meany1)/m

columnOf1 = np.ones( (np.size(X,0),1))
X = np.append(columnOf1, X, 1) # 1 - along column

thetaSet    = np.zeros( (np.size(X,1)) )

iterations =5000 
while iterations >0:
    
    gradientSet = np.zeros( (np.size(X,1)) )
    
    hFnResult = np.dot(X,thetaSet) - y
    
    theta0 = sum( hFnResult* X[:,0]) 
    theta1 = sum( hFnResult* X[:,1])
    theta2 = sum( hFnResult* X[:,2])
    
    thetaSet[0] -= alpha*theta0 / m
    thetaSet[1] -= alpha*theta1 / m
    thetaSet[2] -= alpha*theta2 / m
    
    print thetaSet
    iterations-=1

print thetaSet

# SHOW
projY = np.dot(X,thetaSet)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(fileData[:,0], fileData[:,1], fileData[:,2], c='b', marker='o')
ax.scatter(fileData[:,0], fileData[:,1], projY, c='r', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')


plt.show()

#===============================================================================
# fileData = np.genfromtxt('ex1data1.txt', delimiter = ',')
# 
# X = fileData[:,0:1]
# y = fileData[:,1]
# m = np.size(X)
# 
# columnOf1 = np.ones( (np.size(X),1))
# X = np.append(columnOf1, X, 1)
# 
# thetaSet    = np.zeros( (np.size(X,1)) )
# 
# iterations =1500 
# while iterations >0:
#     
#     gradientSet = np.zeros( (np.size(X,1)) )
#     
#     hFnResult = np.dot(X,thetaSet) - y
#     theta0 = sum( hFnResult* X[:,0]) 
#     theta1 = sum( hFnResult* X[:,1])
#     thetaSet[0] -= alpha*theta0 / m
#     thetaSet[1] -= alpha*theta1 / m
#     
#     #print thetaSet
#     iterations-=1
# 
# print thetaSet
# 
# # SHOW
# projY = np.dot(X,thetaSet)
# 
# plt.plot( fileData[:,0],y,'ro')
# plt.plot( fileData[:,0], projY, 'bo')
# plt.show()
#===============================================================================
 