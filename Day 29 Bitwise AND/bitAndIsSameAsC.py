#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    print(k-1 if (k|k-1) <= n else k-2) 

