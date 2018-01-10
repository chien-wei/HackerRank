#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n3 = (n / 3, n / 3 - 1)[n % 3 == 0]
    n5 = (n / 5, n / 5 - 1)[n % 5 == 0]
    n15 = (n / 15, n / 15 - 1)[n % 15 == 0]
    n3 = int(n3)
    n5 = int(n5)
    n15 = int(n15)
    sum = ((1 + n3) * n3 * 3 >> 1) + ((1 + n5) * n5 * 5 >> 1) - ((1 + n15) * n15 * 15 >> 1);
    sum = int(sum)
    print(sum)