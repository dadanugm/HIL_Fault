#!python
#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
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

data_fix_1 = data_1.reshape(1,datasize)
data_fix_2 = data_2.reshape(1,datasize)
data_fix_3 = data_3.reshape(1,datasize)

# get all data from array and store into list
time = []
fault1_1 = []
fault1_2 = []
fault1_3 = []
fault2_1 = []
fault2_2 = []
fault2_3 = []
fault3_1 = []
fault3_2 = []
fault3_3 = []

for i in range (0,datasize,datashape[1]):
    time.append (data_fix_1[0,i])
    fault1_1.append(data_fix_1[0,i+1])
    fault1_2.append(data_fix_1[0,i+2])
    fault1_3.append(data_fix_1[0,i+3])
    fault2_1.append(data_fix_2[0,i+1])
    fault2_2.append(data_fix_2[0,i+2])
    fault2_3.append(data_fix_2[0,i+3])
    fault3_1.append(data_fix_3[0,i+1])
    fault3_2.append(data_fix_3[0,i+2])
    fault3_3.append(data_fix_3[0,i+3])

plt.figure("3 Phase fault")
phs1 = plt.subplot(311)
phs1.set_title("fault 1")
phs1.set_ylabel("volt")
phs1.set_xlabel("time")

phs2 = plt.subplot(312)
phs2.set_title("fault 2")
phs2.set_ylabel("volt")
phs2.set_xlabel("time")

phs3 = plt.subplot(313)
phs3.set_title("fault 3")
phs3.set_ylabel("volt")
phs3.set_xlabel("time")


#for j in range (datashape[0]):
phs1.plot(time,fault1_1,color='green',linewidth=1)
phs1.plot(time,fault1_2,color='blue',linewidth=1)
phs1.plot(time,fault1_3,color='red',linewidth=1)
phs2.plot(time,fault2_1,color='green',linewidth=1)
phs2.plot(time,fault2_2,color='blue',linewidth=1)
phs2.plot(time,fault2_3,color='red',linewidth=1)
phs3.plot(time,fault3_1,color='green',linewidth=1)
phs3.plot(time,fault3_2,color='blue',linewidth=1)
phs3.plot(time,fault3_3,color='red',linewidth=1)

#plt.pause(0.0001)

plt.show()
