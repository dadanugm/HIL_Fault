#!python
#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tables
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

fig = plt.figure("3 phase fault")
ax_1 = plt.subplot(311)
ax_2 = plt.subplot(312)
ax_3 = plt.subplot(313)

ax_1.set_xlim(0, 0.7)
ax_1.set_ylim(-1000000, 1500000)
ax_2.set_xlim(0, 0.7)
ax_2.set_ylim(-1500000, 2500000)
ax_3.set_xlim(0, 0.7)
ax_3.set_ylim(-1200000, 2000000)

line1_1, = ax_1.plot([],[],'g-')
line1_2, = ax_1.plot([],[],'r-')
line1_3, = ax_1.plot([],[],'b-')
line2_1, = ax_2.plot([],[],'g-')
line2_2, = ax_2.plot([],[],'r-')
line2_3, = ax_2.plot([],[],'b-')
line3_1, = ax_3.plot([],[],'g-')
line3_2, = ax_3.plot([],[],'r-')
line3_3, = ax_3.plot([],[],'b-')

def animate(num,time,phase11,phase12,phase13,phase21,phase22,phase23,phase31,phase32,phase33,line1_1,line1_2,line1_3,line2_1,line2_2,line2_3,line3_1,line3_2,line3_3):
    line1_1.set_data(time[:num],phase11[:num])
    line1_2.set_data(time[:num],phase12[:num])
    line1_3.set_data(time[:num],phase13[:num])
    line2_1.set_data(time[:num],phase21[:num])
    line2_2.set_data(time[:num],phase22[:num])
    line2_3.set_data(time[:num],phase23[:num])
    line3_1.set_data(time[:num],phase31[:num])
    line3_2.set_data(time[:num],phase32[:num])
    line3_3.set_data(time[:num],phase33[:num])
    #line.set_ydata(phase1[:num])
    #return line,

ani = animation.FuncAnimation (fig,animate,frames=500,interval=1,fargs=[time,phase11,phase12,phase13,phase21,phase22,phase23,phase31,phase32,phase33,line1_1,line1_2,line1_3,line2_1,line2_2,line2_3,line3_1,line3_2,line3_3],blit=False)

plt.show()
