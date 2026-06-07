# Requires: pip install numpy
# numpy is not part of the standard library; install it before running this file.
import numpy

n = 5
x = numpy.prod([i for i in range(1, n + 1)])
print(x)
