#!/usr/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    
    
    j, i = 0, 1
    check = q[j]
    count, total = 0, 0

    while i < len(q):

        if check > q[i]:
            count += 1
        
        if i == len(q) - 1 and j != len(q)-2:
            j += 1
            check = q[j]
            i = j
            
            if count > 2:
                return('Too chaotic.')
            total += count
            count = 0
        i +=1
    
    return(total)

        

if __name__ == '__main__':

    q = [2, 1, 5, 3, 4]
    q2 = [2, 5, 1, 3, 4]
    print(minimumBribes(q))
    print(minimumBribes(q2))