import numpy as np
import time
import sys

SIZE = 10

l1 = range(SIZE)
l1 = list(range(SIZE))
print("python list l1: ", l1)
print(l1 + l1)

sys.exit()

l2 = range(SIZE)

a1 = np.arange(SIZE)
print("numpy array a1: ", a1)
a2 = np.arange(SIZE)

#python list
start = time.time()
result = [(x+y) for x,y in zip(l1, l2)]
print("python list took: ", (time.time() - start) *1000)
print("resultado lista: " + str(result))
#result = l1 + l2

#numpy array
start = time.time()
result = a1 + a2
print("numpy list took: ", (time.time() - start) *1000)
print("resultado array: " + str(result))
