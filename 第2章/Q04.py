#Q4
import numpy as np
x = np.zeros(10,dtype=np.int32)
x[::2] = 1
print(x)

x = np.zeros(10,dtype = np.int32)
x[np.arange(10) % 2 == 0] = 1 #ブーリアンマスク
print(x)