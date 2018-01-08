#!/bin/python3

import sys


N = int(input().strip())
if N == 2 or N == 4 or (N > 20 and N % 2 == 0):
    print('Not Weird')
else:
    print('Weird')