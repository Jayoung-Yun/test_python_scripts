import numpy as np
element = 'oxygen'
print ('first three characters:'), element[0:3]
print ('last three characters :'), element[3:6]
print ('element[ :4]  :'), element[:4]
print ('element[4: ]  :'), element[4:]
print ('element[ : ]  :'), element[:]
print ('element[-1]   :'), element[-1]
print ('element[-2]   :'), element[-2]
print ('element[1:-1] :'), element[1:-1]
print element[0], element[-1]
print element[1], element[-2]
print element[2], element[-3]
print element[3], element[-4]
print element[4], element[-5]
print element[5], element[-6]

#---- Thin Slices ----
print element[3:3]


#data = numpy.loadtxt(fname='./data/inflammation-01.csv', delimiter=',')
data = np.loadtxt(fname='./data/inflammation-01.csv', delimiter=',')
print data   [3:3, 4:4]
print data   [3:3, :]

import matplotlib.pyplot 
fig = matplotlib.pyplot.figure(figsize=(4, 4))
axes3 = fig.add_subplot(1,1,1)
axes3.set_ylabel('min')
axes3.plot(np.min(data, axis=0))
matplotlib.pyplot.show()
#axes3.set_ylim(0,6)

min_data=np.min(data,axis=0)
axes3.set_ylabel('min')
axes3.plot(min_data)
#axes3.set_ylim(np.min(min_data), np.max(min_data) *1.1)
#matplotlib.pyplot.show()
