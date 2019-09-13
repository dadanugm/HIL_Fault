#!python
#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
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

fig, ax = plt.subplots()
ax.set_xlim(0,0.7)
ax.set_ylim(-1000000,1200000)

line1, = ax.plot([],[],'g-')
line2, = ax.plot([],[],'r-')
line3, = ax.plot([],[],'b-')

def animate(num,time,phase1,phase2,phas3,line1,line2,line3):
    line1.set_data(time[:num],phase1[:num])
    line2.set_data(time[:num],phase2[:num])
    line3.set_data(time[:num],phase3[:num])
    #line.set_ydata(phase1[:num])
    #return line,

ani = animation.FuncAnimation (fig,animate,frames=500,interval=1,fargs=[time, phase1, phase2, phase3, line1, line2, line3],blit=False)

plt.show()
