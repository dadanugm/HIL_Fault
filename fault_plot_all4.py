#!python
#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tables
from celluloid import Camera

file1 = tables.open_file('data1.mat')
file2 = tables.open_file('data2.mat')
file3 = tables.open_file('data3.mat')

getdata1 = file1.root.data1[:]
getdata2 = file2.root.data2[:]
getdata3 = file3.root.data3[:]

data_1 = np.array(getdata1)
data_2 = np.array(getdata2)
data_3 = np.array(getdata3)

datasize = int(data_1.size)
datashape = data_1.shape
print (datashape[0])
print (datashape[1])

data_fix1 = data_1.reshape(1,datasize)
data_fix2 = data_2.reshape(1,datasize)
data_fix3 = data_3.reshape(1,datasize)

# get all data from array and store into list
time = []
phase11 = []
phase12 = []
phase13 = []
phase21 = []
phase22 = []
phase23 = []
phase31 = []
phase32 = []
phase33 = []

for i in range (0,datasize,datashape[1]):
    time.append (data_fix1[0,i])
    phase11.append (data_fix1[0,i+1])
    phase12.append (data_fix1[0,i+2])
    phase13.append (data_fix1[0,i+3])
    phase21.append (data_fix2[0,i+1])
    phase22.append (data_fix2[0,i+2])
    phase23.append (data_fix2[0,i+3])
    phase31.append (data_fix3[0,i+1])
    phase32.append (data_fix3[0,i+2])
    phase33.append (data_fix3[0,i+3])

fig, ax = plt.subplots(3)
camera = Camera(fig)

for j in range (datashape[0]):
    ax[0].plot(time[j],phase11[j],'g-')
    ax[0].plot(time[j],phase12[j],'g-')
    ax[0].plot(time[j],phase13[j],'g-')
    ax[1].plot(time[j],phase21[j],'g-')
    ax[1].plot(time[j],phase22[j],'g-')
    ax[1].plot(time[j],phase23[j],'g-')
    ax[2].plot(time[j],phase31[j],'g-')
    ax[2].plot(time[j],phase32[j],'g-')
    ax[2].plot(time[j],phase33[j],'g-')
    camera.snap()

animation = camera.animate() 


