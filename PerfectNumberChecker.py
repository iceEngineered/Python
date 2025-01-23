'''
Determine whether a number is a "perfect number"
= all the divisors of it add to it
1 + 2 + 3 = 6
1 + 2 + +4 + 7 + 14 = 28
'''

import sys
input = int(sys.argv[1])
divisors = []
for x in range(1, input):
 if input%x == 0:
  divisors.append(x)

sum=0
math = ""
for x in divisors:
 sum+=x
 if math == "":
  math+=str(x)
 else:
  math+="+"
  math+=str(x)

math+="="
math+=str(sum)
print(math)

if sum == input:
 print(input," is a perfect number")
else:
 print(input,"is not a perfect number")
