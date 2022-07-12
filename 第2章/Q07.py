import numpy as np
x = np.arange(100) + 1
num = x.astype(np.object)

num[2::3] = "Fizz"
num[4::5] = "Buzz"
num[14::15] = "FizzBuzz"

print(num)