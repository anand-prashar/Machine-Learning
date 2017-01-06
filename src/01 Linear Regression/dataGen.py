'''
Created on Jan 4, 2017

@author: anand
'''
fw = open('linreg2.txt','w')

for y in range(200):
    row = str(2*y)+','+str(y)+','+str(2*y+y+3.5)+'\n'
    fw.write(row)

fw.close()
print 'done'    
  