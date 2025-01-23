
"""
For a given positive integer n:
	1.	If n is even, divide it by 2.
	2.	If n is odd, multiply it by 3 and add 1.
	3.	Repeat this process until n becomes 1.

The challenge is to:
	1.	Write a program to compute the sequence for any starting number n.
	2.	Count how many steps it takes to reach 1.
	3.	(Optional) Identify the number below a certain threshold (e.g., 1,000) that produces the longest sequence.
"""

import sys

input = int(sys.argv[1])
x = input
sequence = []
steps = 0
while (x != 1):
 sequence.append(x)
 steps += 1
 if x % 2 == 0:
  y = x/2
  print(x,"/2=",y)
 else:
  y = (x*3)+1
  print("(",x,"*3)+1")
 x = y

print("Steps = ",steps)
