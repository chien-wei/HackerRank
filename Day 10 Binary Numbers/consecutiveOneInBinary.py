#!/bin/python3

import sys


n = int(input().strip())
s = bin(n)[2:]
result = 0
count = 0
for c in s:
    if c == '1':
        count += 1
    else:
        result = max(count, result)
        count = 0
result = max(count, result)
print(result)