'''
Check if a number is an armstrong number
An Armstrong number (or narcissistic number) is a number that is equal to the sum of its own digits 
each raised to the power of the number of digits. For example:
153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
9474 is an Armstrong number because 9^4 + 4^4 + 7^4 + 4^4 = 9474.
'''

import sys
input = sys.argv[1]
digits = []
for x in input:
 digits.append(int(x))

math = ""
sum = 0
for x in digits:
 sum+=x**len(digits)
 if math != "":
  math+=" + "
 math+=str(x)
 math+="^"
 math+=str(len(digits))

math+=" = "
math+=str(sum)
print(math)

if (sum == int(input)) :
 print(input," is an armstrong number")
else:
 print(input," is not an armstrong number")
