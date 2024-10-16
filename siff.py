'''
    this block of code showa the difference between list in python
    and array in numpy.
'''
import numpy as np
import time

# Python list
python_list = list(range(1000000))
start = time.time()
python_result = [x * 2 for x in python_list]
print("Python List Time:", time.time() - start)

# Numpy array
numpy_array = np.arange(1000000)
start = time.time()
numpy_result = numpy_array * 2
print("Numpy Array Time:", time.time() - start)