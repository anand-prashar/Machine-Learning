'''
Created on Jan 5, 2017

@author: anand
'''
## USE 5TH COLUMN AS CLASSIFICATION LABEL FOR records

import numpy as np
import math
def sigmoid_function(thetaTx):
    
    gX = []
    
    for thetaTx_row in thetaTx:
        expFnResult = 1/(1+ math.pow(math.e, -thetaTx_row))
        gX.append(expFnResult)
        
    return  np.array(gX)
  
inputData = np.genfromtxt('classification.txt', delimiter = ',')
inputData = np.delete(inputData,3,1)  # delete 4th column, (1 => along column)

X = inputData[:,0:3]
y = inputData[:,3]
alpha = 0.01
m = np.size(X,0)

columnOf1 = np.ones( (np.size(X,0),1))
X = np.append(columnOf1, X, 1)          # 1 - along column

thetaSet    = np.ones( (np.size(X,1)) )
iterations = 7000

while iterations >=0:
    
    thetaTx = np.dot(X,thetaSet)
    hFnResult = sigmoid_function(thetaTx)
    
    gradientSet = np.zeros( (np.size(X,1)) )
    errorVector = hFnResult - y
    
    theta0 = sum( errorVector * X[:,0])
    theta1 = sum( errorVector * X[:,1])
    theta2 = sum( errorVector * X[:,2])
    theta3 = sum( errorVector * X[:,3])
    
    thetaSet[0] -= (alpha/m)*theta0
    thetaSet[1] -= (alpha/m)*theta1
    thetaSet[2] -= (alpha/m)*theta2
    thetaSet[3] -= (alpha/m)*theta3
    
    print thetaSet
    iterations-=1
    

print 'DONE'    