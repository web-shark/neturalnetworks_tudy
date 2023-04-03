import numpy as np
from matplotlib import pyplot as plt
x = np.random.random((2000, 2))
# x = np.random.randint(2,size=(100,2))
# y = np.logical_xor(x[:,0], x[:,1])
# print(f)
y = np.logical_xor(np.around(x[:,0]), np.around(x[:,1]))
# print(h)
print(x)
print(y)
plt.scatter(x[:,0], x[:,1], c=y)
plt.show()