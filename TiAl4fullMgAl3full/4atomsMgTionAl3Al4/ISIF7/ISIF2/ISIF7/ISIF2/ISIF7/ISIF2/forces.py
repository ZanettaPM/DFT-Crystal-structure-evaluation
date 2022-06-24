import numpy as np

dataFile = open('OUTCAR', 'r')
dataLines = dataFile.readlines()
counter = 0                                         # For counting the line number
forceIndexList = []                                 # Container for force index line
for i in dataLines:
    counter = counter + 1
    a = i.strip()
    b = a.split()
    if (len(b) != 0):
        if (b[0] == 'POSITION'):
            forceIndexList.append(counter)

counter = 0
fxList = []
fyList = []
fzList = []
for i in dataLines[forceIndexList[-1] + 1:forceIndexList[-1] + 1 + 256]:
    counter = counter + 1
    a = i.strip()
    b = a.split()
    fxList.append(float(b[3]))
    fyList.append(float(b[4]))
    fzList.append(float(b[5]))

dataFile.close()

print (min(fxList))
print (max(fxList))
print ('-----------------------------')
print (min(fyList))
print (max(fyList))
print ('-----------------------------')
print (min(fzList))
print (max(fzList))

