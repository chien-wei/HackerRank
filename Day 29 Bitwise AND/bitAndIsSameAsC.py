#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    _max = 0
    for a in range(1, n+1):
        for b in range(a+1, n+1):
            v = a & b
            if v >= k:
                continue
            _max = max(_max, v)
    print(_max)
