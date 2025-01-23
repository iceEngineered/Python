#Takes one number from CLI input as X and calculates the Xth number in the fibonacci sequence

import sys
a = int(sys.argv[1])
b = a-2
x = 0
y = 1
sequence = [0,1]
for i in range(b):
 z = x+y
 print(x,"+",y,"=",z)
 x = y
 y = z

print("So number ",a," in the Fibonacci Sequence is ",z)
