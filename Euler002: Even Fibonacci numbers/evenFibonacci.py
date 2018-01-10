#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n < 2:
        print(0)
    a = 1
    b = 2
    sum = 0
    while b < n:
        a, b = b, a+b
        if a % 2 == 0:
            sum += a
    if b < n and b % 2 == 0:
        sum += b
    print(sum)