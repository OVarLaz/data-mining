import numpy as np
from scipy.spatial.distance import euclidean

import fastdtw

x = np.array([[1,1,2], [2,2,3], [3,3,4], [4,4,5], [5,5,6]])
y = np.array([[2,2,0], [3,3,2], [4,4,6]])

print x

def reduce_by_half(x):
    return [(x[i] + x[1+i]) / 2 for i in range(0, len(x) - len(x) % 2, 2)] 


print reduce_by_half(x)
print np.asanyarray(x, dtype='float')
print x.ndim
print "-----------***** fastdtw"
distance, path = fastdtw.fastdtw(x, y, dist=euclidean)
print(distance)