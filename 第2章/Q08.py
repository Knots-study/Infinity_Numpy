#Q8
import numpy as np
x = np.arange(100) + 1
num = x.astype(np.object)

num[x%3==0] = "アホ"
num[x%10 == 3] = "アホ"
num[x//10 == 3] = "アホ"
print(num)