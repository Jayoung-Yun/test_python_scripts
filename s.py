import numpy

print "Welcome to the load data file, I am your computer."
print "I am going to try to open the file some_data.csv"
my_data = numpy.loadtxt(fname='some_data.csv', delimiter=',')

print "let me show you what I understood:"
print my_data
