from __future__ import print_function

num = 25 # a number above 2 and below 10

for test in range(2,num):
  if num % test == 0 and num != test:
    print(num,'equals',test, '*', num/test)
    print(num,'is not a prime number')
    break

else:
  print(num,'is a prime number.')

