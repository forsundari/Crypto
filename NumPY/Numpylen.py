''''''
import numpy

import time

import sys

s = range(1000)

print(sys.getsizeof(5) * len(s))

D = numpy.arange(1000)

print(D.size*D.itemsize)
''''''

import numpy

print(numpy.__version__)

Name = [2,4,6,8,10]

print(Name)

numpy1 = numpy.array(Name)

print(numpy1)