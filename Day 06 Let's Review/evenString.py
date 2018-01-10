#!/bin/python3

import sys


t = int(input().strip())
for i in range(t):
    s = input()
    print(s[::2], s[1::2])