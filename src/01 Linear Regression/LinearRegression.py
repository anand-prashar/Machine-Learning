'''
Created on Jan 4, 2017

@author: anand

t0 + t1.x1 + t2.x2 = 0

'''
import numpy as np
import matplotlib.pyplot as plt

limitTrainingSize = 2000
alpha = 0.1


#===============================================================================
# data3D = np.genfromtxt('linreg.txt', delimiter = ',')
# trainData_features= data3D[:limitTrainingSize,[0,1]]
# trainData_output  = data3D[:limitTrainingSize,[2]]
# testData_features = data3D[limitTrainingSize:,[0,1]]
# testData_output   = data3D[limitTrainingSize:,[2]]
# 
# thetaVector = np.ones( (np.size(data3D,1) +1,1))  # n is 1 more than no of features/columns
# 
# oldThetaVector = np.copy(thetaVector)
# firstRun = True
# 
# while firstRun or oldThetaVector != thetaVector:
#     
#     for
#===============================================================================

trainData_features= []
trainData_output  = []
testData_features = []
testData_output   = []
x = []
y = []

currThetaList = [1,1,1]
#[0.025421601093160, 1.0770710864982744, 3.97983834021892] #

prevThetaList = currThetaList

fileReader = open('linreg.txt')
rowCount = 1
for row in fileReader:
    f1,f2,op = row.split(',')
    x.append(f1)
    y.append(f2)
    
    if rowCount <= limitTrainingSize:
        trainData_features.append([1, float(f1),float(f2) ])
        trainData_output.append([float(op)])
    else:
        testData_features.append([1, float(f1),float(f2)])
        testData_output.append([float(op)]) 
    rowCount+=1
        
plt.plot(x,y,'ro')
plt.show()

firstRun = True
m = len(trainData_features)

while firstRun or (prevThetaList != currThetaList):
    
    gradientList = [0,0,0]
    
    for rowIndex in range(len(trainData_features)):
        fx = 0
        for i in range( len(currThetaList)):
            fx += trainData_features[rowIndex][i]* currThetaList[i]
        
        gradientList[0] += (fx-trainData_output[rowIndex][0]   )
        gradientList[1] += (fx-trainData_output[rowIndex][0]   )* trainData_features[rowIndex][1]
        gradientList[2] += (fx-trainData_output[rowIndex][0]   )* trainData_features[rowIndex][2]
            
    #after each iteration over train dataset
    prevThetaList = currThetaList[:]
    for index in range(len(prevThetaList)):
        currThetaList[index] = currThetaList[index] - (alpha*gradientList[index] /m)
    
    firstRun = False
    print currThetaList  

#===============================================================================
# for index in range( len(trainData_features)):
#     prediction =   currThetaList[0]*trainData_features[index][0] \
#                  + currThetaList[1]*trainData_features[index][1] \
#                  + currThetaList[2]*trainData_features[index][2]
#     
#     print (prediction-trainData_output[i][0])             
#===============================================================================