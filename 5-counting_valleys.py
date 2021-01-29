#!/usr/bin/python3


import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):

    if steps != len(path):
        return
        
    count_valleys = 0
    up_and_down = 0

    for step in path:
        if step == "U":
            up_and_down += 1
        
        elif step == 'D' and up_and_down == 0:
            count_valleys += 1
            up_and_down -= 1

        else:
            up_and_down -= 1

    return(count_valleys)

if __name__ == '__main__':

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)