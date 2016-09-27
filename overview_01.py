import numpy
numpy.loadtxt(fname='./data/inflammation-01.csv', delimiter=',')
print numpy.loadtxt(fname='./data/inflammation-01.csv', delimiter=',')

weight_kg = 55
print(weight_kg)
print weight_kg

print('weight in pounds:', 2.2*weight_kg)

weight_kg = 57.5
print('weight in kilograms is now:', weight_kg)

weight_lb=2.2*weight_kg
print('weight in kilograms:', weight_kg, 'and in pounds:', weight_lb)

weight_kg=100.0
print('weight in kilograms is now:', weight_kg, 'and weight in pounds is still:', weight_lb)

data = numpy.loadtxt(fname='./data/inflammation-01.csv', delimiter=',')
print(data)

print ('type(data) :'), (type(data))

print ('data.dtype :'), (data.dtype)

print ('data.shape :'), (data.shape)

print ('first value in data  :'), data[0,0]

print ('middle value in data :'), data[30,20]

print ('--------------[0:4 , 0:10]---------------')
print (data[0:4, 0:10])
print ('--------------[5:10, 0:10]---------------')
print (data[5:10, 0:10])

small = data[:3, 36:]
print ('small is:')
print (small)

doubledata = data *2.0

print ('original:')
print (data[:3, 36:])
print ('doubledata:')
print (doubledata[:3, 36:])

tripledata = doubledata + data
print ('tripledata:')
print (tripledata[:3, 36:])

print ('numpy.mean(data):'), (numpy.mean(data))

# Not All Functions Have Input
import time
print ('Current time :'), (time.ctime())

print ('-----------------------------------------')
maxval, minval, stdval = numpy.max(data), numpy.min(data), numpy.std(data)
print ('maximum inflammation:'), maxval
print ('minimum inflammation:'), minval
print ('standard deviation  :'), stdval


# Mystery Functions in IPython
patient_0 = data[0, :] # 0 on the first axis, everything on the second
print ('maximum inflammation for patient 0:'), patient_0.max()

print ('maximum inflammation for patient 2:'), numpy.max(data[2,:])

print ('-----------------------------------------')
print ('numpy.mean(data, axis=0)')
print (numpy.mean(data, axis=0))


print (numpy.mean(data, axis=0).shape)

print ('-----------------------------------------')
print ('numpy.mean(data, axis=1)')
print (numpy.mean(data, axis=1))


print ('-----------------------------------------')
import matplotlib.pyplot
image = matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show()


ave_inflammation = numpy.mean(data, axis=0)
ave_plot = matplotlib.pyplot.plot(ave_inflammation)
matplotlib.pyplot.show()

max_plot = matplotlib.pyplot.plot(numpy.max(data, axis=0))
matplotlib.pyplot.show()

min_plot = matplotlib.pyplot.plot(numpy.min(data, axis=0))
matplotlib.pyplot.show()
