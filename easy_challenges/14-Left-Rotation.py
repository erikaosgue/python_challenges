#!/usr/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    count = 0
    while count < d:
        num = a.pop(0)
        a.append(num)
        count += 1
    return a


if __name__ == '__main__':
    
    a = [1, 2, 3, 4, 5]
    d = 4 # Move four places to the left
    print(rotLeft(a, d))