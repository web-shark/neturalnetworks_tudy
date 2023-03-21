from datetime import datetime

import numpy as np




a = np.random.random((1000,1000))
b = np.random.random((1000,1000))
print(a,b)
m = len(a) # a: m × n
n = len(b) # b: n × k
k = len(b[0])
t0 = datetime.now()
d = a.dot(b)
dt1 = datetime.now() - t0
print(d)
c = [[None for _ in range(k)] for _ in range(m)]    # c: m × k
t0 = datetime.now()
for i in range(m):
    for j in range(k):
        c[i][j] = sum(a[i][kk] * b[kk][j] for kk in range(n))
dt2 = datetime.now() - t0
print(c)
print("dt1 / dt2:", dt1.total_seconds() / dt2.total_seconds())
