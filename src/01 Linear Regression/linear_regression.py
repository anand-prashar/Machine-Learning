'''
Created on Jan 5, 2017

@author: anand
'''
alpha = 0.001

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fileData = np.genfromtxt('ex1data2.txt', delimiter = ',')

X = fileData[:,0:2]
y = fileData[:,2]
m = np.size(X)

meanVector  = np.ndarray.mean(X,0)
sigmaVector = np.ndarray.std(X,0)

for row in X:
    for col in range(np.size(X,1)):
        row[col] = (row[col]- meanVector[col])/sigmaVector[col]
    
columnOf1 = np.ones( (np.size(X,0),1))
X = np.append(columnOf1, X, 1) # 1 - along column

thetaSet    = np.zeros( (np.size(X,1)) )

iterations =150000
while iterations >0:
    
    gradientSet = np.zeros( (np.size(X,1)) )
    
    errorValueVector = np.dot(X,thetaSet) - y
    
    theta0 = sum( errorValueVector* X[:,0]) 
    theta1 = sum( errorValueVector* X[:,1])
    theta2 = sum( errorValueVector* X[:,2])
    
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
ax.scatter(fileData[:,0], fileData[:,1], projY, c='g', marker='o')

# find Solution for below data point [1, x, y]
testResult = np.dot([1,-0.44127326, -0.223658],thetaSet)
ax.scatter( -0.44127326, -0.223658,testResult, c = 'r', marker = 'o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

print 'TEST RESULT=', testResult
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
#     errorValueVector = np.dot(X,thetaSet) - y
#     theta0 = sum( errorValueVector* X[:,0]) 
#     theta1 = sum( errorValueVector* X[:,1])
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
 