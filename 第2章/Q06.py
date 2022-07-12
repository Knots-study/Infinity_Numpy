import numpy as np
x = np.arange(100) + 1
num = x.astype(np.object)#numpy配列に文字列は代入できないため、np.objectに型変換

num[x%3  == 0] = "Fizz"
num[x%5  == 0] = "Buzz"
num[x%15 == 0] = "FizzBuzz"

print(num)