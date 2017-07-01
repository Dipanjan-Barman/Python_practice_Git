#!/usr/bin/env python3

import random

x = random.sample(range(100),30)
y = random.sample(range(60),25)

a = []

for i in x:
    if i in y and i not in a:
       a.append(i)

print("\n" '\x1b[2;30;42m' + 'List 1:' + '\x1b[0m' + str(x))
print("\n" '\x1b[2;30;42m' + 'List 2:' + '\x1b[0m' + str(y))
print("\n" '\x1b[2;30;43m' + 'Common elements:' + '\x1b[0m' + str(a) + "\n")

