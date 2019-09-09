#!python
#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import tables
file = tables.open_file('data1.mat')
getdata = file.root.data1[:]
data = np.array(getdata)
datasize = int(data.size)
datashape = data.shape
datashape = datashape[1]
data_fix = data.reshape(1,datasize)

# get all data from array and store into list
time = []
phase1 = []
phase2 = []
phase3 = []

for i in range (0,datasize,datashape):
    time.append (data_fix[0,i])
    phase1.append (data_fix[0,i+1])pi
    phase2.append (data_fix[0,i+2])
    phase3.append (data_fix[0,i+3])

plt.plot(time,phase1)
plt.plot(time,phase2)
plt.plot(time,phase3)
plt.show()
