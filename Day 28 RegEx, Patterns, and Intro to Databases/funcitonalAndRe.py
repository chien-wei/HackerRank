#!/bin/python3

import sys
from itertools import *
import re

N = int(input().strip())
name = []
email = []
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    name.append(firstName)
    email.append(emailID)

print("\n".join(sorted(list(filter(lambda y: y, map(lambda x: x[0] if(re.search(r'[a-z]+@gmail.com', x[1])) else None, zip(name, email)))))))