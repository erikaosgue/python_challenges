#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    last_cloud_seen = 0
    jump = 0
    length_jump =0

    for i, curr_cloud in enumerate(c):
        
        if i != 0:
            length_jump += 1
        
        if last_cloud_seen == 0 and curr_cloud == 1 and length_jump == 2:
            jump += 1
            length_jump = 1 

        elif length_jump == 2 or i == len(c) - 1:
            jump += 1
            length_jump = 0
        
        last_cloud_seen = curr_cloud


        
    return(jump)

if __name__ == '__main__':

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)