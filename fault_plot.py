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
#datashape = datashape[1]
print (datashape[0])
print (datashape[1])
data_fix = data.reshape(1,datasize)

# get all data from array and store into list
time = []
phase1 = []
phase2 = []
phase3 = []



for i in range (0,datasize,datashape[1]):
    time.append (data_fix[0,i])
    phase1.append (data_fix[0,i+1])
    phase2.append (data_fix[0,i+2])
    phase3.append (data_fix[0,i+3])

plt.figure()
for j in range (datashape[0]):
    plt.plot(time[j],phase1[j],'g--',color='green',marker='.',linewidth=2,markersize=2,linestyle='-')
    plt.plot(time[j],phase2[j],'b--',color='blue',marker='.',linewidth=2,markersize=2,linestyle='-')
    plt.plot(time[j],phase3[j],'r--',color='red',marker='.',linewidth=2,markersize=2,linestyle='-')
    plt.draw()
    plt.pause(0.0001)

#plt.figure()
plt.show()
