#!/usr/bin/python3

"""

"""

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    
    count = 0
    for i in range(len(q)):
        result = q[i] - (i + 1)

        if (result >= 3):
            print("Too chaotic")
            return

        for j in range(max(q[i] - 1, 1), i+1):
            # print("> ", q[i] - 1, i+1, q[i], max(q[i] - 1, 1))
            if (q[j - 1] > q[i]):
                count += 1
    print(count)

    
    
if __name__ == '__main__':
    # 3 the order of the people in the line
    # Initially the order was from 1 2 3 4 5 ...
    # Later people move and that is the order of q

    q_1 = [1, 2, 3, 5, 4, 6, 7,8]

    q_2 = [2, 1, 5, 3, 4]

    q_3 = [2, 5, 1, 3, 4]

    q_4 = [1, 2, 5, 3, 7, 8, 6, 4] # 7

    # minimumBribes(q_1) # 1
    # minimumBribes(q_2) # 3
    # minimumBribes(q_3) # Too chaotic
    minimumBribes(q_4) # 7
