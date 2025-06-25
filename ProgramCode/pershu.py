import numpy as np 
from  numpy import random
arr = np.array([3,462,342,54])
random.shuffle(arr)
print(arr)

print(random.permutation(arr))
