#!/usr/bin/env python3

from math import sqrt

num = int(input("Enter an integer number: "))

divisors = []
max_disvisor = int(sqrt(abs(num)))
range_num = range(1,max_disvisor+1)

for i in range_num:
    if num % i == 0:
        divisors.append(i)
        divisors.append(int(abs(num)/i))

if num > 0:
    print("\nThe list of divisors of " + str(num) + ":")
    print (sorted(set(divisors)))
else:
    divisors[:] = [x * -1 for x in divisors]
    print("\nThe list of divisors of " + str(num) + ":" + "\n")
    print (sorted(set(divisors), reverse=True))
