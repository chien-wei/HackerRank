#!/bin/python3

import sys


arr = []
result = -9*7-1
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)
for i in range(1,5):
    for j in range(1,5):
        cur = arr[i][j] + arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
        result = max(result, cur)
print(result)