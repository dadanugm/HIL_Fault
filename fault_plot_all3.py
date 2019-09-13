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

plt.figure("3 phase fault")
plt.xlim(0, 0.7)
plt.ylim(-1000000, 1200000)
ax_1 = plt.subplots(311)
ax_2 = plt.subplots(312)
ax_3 = plt.subplots(313)


line1_1 = ax_1.plot(time,phase11,'g-')
line1_2 = ax_1.plot(time,phase12,'r-')
line1_3 = ax_1.plot(time,phase13,'b-')
line2_1 = ax_2.plot(time,phase21,'g-')
line2_2 = ax_2.plot(time,phase22,'r-')
line2_3 = ax_2.plot(time,phase23,'b-')
line3_1 = ax_3.plot(time,phase31,'g-')
line3_2 = ax_3.plot(time,phase32,'r-')
line3_3 = ax_3.plot(time,phase33,'b-')

def animate(num,time,phase11,phase12,phase13,phase21,phase22,phase23,phase31,phase32,phase33,line1_1,line1_2,line1_3,line2_1,line2_2,line2_3,line3_1,line3_2,line3_3):
    line1_1.set_data(time[:num],phase1_1[:num])
    line1_2.set_data(time[:num],phase1_2[:num])
    line1_3.set_data(time[:num],phase1_3[:num])
    line2_1.set_data(time[:num],phase2_1[:num])
    line2_2.set_data(time[:num],phase2_2[:num])
    line2_3.set_data(time[:num],phase2_3[:num])
    line3_1.set_data(time[:num],phase3_1[:num])
    line3_2.set_data(time[:num],phase3_2[:num])
    line3_3.set_data(time[:num],phase3_3[:num])
    #line.set_ydata(phase1[:num])
    #return line,

ani = animation.FuncAnimation (fig,animate,frames=500,interval=1,fargs=[time,phase11,phase12,phase13,phase21,phase22,phase23,phase31,phase32,phase33,line1_1,line1_2,line1_3,line2_1,line2_2,line2_3,line3_1,line3_2,line3_3],blit=False)

plt.show()
