'''
Created on Jan 7, 2017

@author: anand
'''
import numpy as np
from scipy import io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

def getImageMatrix(arr):
    tempRow = []
    for i in range(20):
        tempRow.append('')
    sampleImage = []
    for i in range(20):
        sampleImage.append(tempRow[:])
    
    itr=0
    offset = min(arr)
    
    for i in range(20):
        for j in range(20):
            sampleImage[i][j] = arr[itr]-offset#0.0575151143791 
            itr+=1
    return sampleImage

imageMatrix = io.loadmat('ex3data1.mat')

X = imageMatrix['X']
y = imageMatrix['y']

#print np.size(X,1)


imageList = []

itr = 0
for i in range(5):
    imgName = str(i)+'.png'
    for j in range(20):
        image = getImageMatrix( X[i])
        #imgplot = plt.imshow(image, cmap='gray')
        #plt.axis('off')
        #plt.savefig(imgName)
        imageList+=image

imgplot = plt.imshow(getImageMatrix(X[4999]), cmap='gray')
plt.axis('off')
plt.show()
plt.savefig('OP.png')
print 'Done printing image'

