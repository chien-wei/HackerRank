#!/bin/python3

def _12to24(s):
    # Complete this function
    if s[-2:] == "AM" and s[0:2] == "12":
        s = "00" + s[2:-2]
    elif s[-2:] == "PM" and s[0:2] == "12":
        s = "12" + s[2:-2]
    elif s[-2:] == "PM":
        s = str(int(s[0:2]) + 12) + s[2:-2]
    else:
        s = s[:-2]
    return s

