#!/bin/python3

import sys

def canConstruct(a):
    # Return "Yes" or "No" denoting whether you can construct the required number.
    sumOfDigit = 0
    for i in a:
        while i != 0:
            sumOfDigit += i % 10
            i = int(i / 10)
    return ("No", "Yes")[sumOfDigit % 3 == 0]

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        a = list(map(int, input().strip().split(' ')))
        result = canConstruct(a)
        print(result)