'''
Determine whether a number is a prime number or not
'''

import sys
import math
input = int(sys.argv[1])
isAPrime=True

if input == 0:
 print("0 is not a prime number")
 isAPrime=False
elif input == 1:
 print("1 is not a prime number")
 isAPrime=False
elif input == 2:
 isAPrime=True
elif input%2 == 0:
 print(input," is an even number, therefore not prime")
 isAPrime=False
else:
 possibles = []
 for x in range(2,int(math.sqrt(input)+1)):
  if (x%2 != 0):
   possibles.append(x)
 for x in possibles:
  y = input%2
  if y == 0:
   print(input," isn't a prime since ",x," divides it")
   isAPrime=False
if isAPrime != False:
 print(input," is a prime")
