#!/usr/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    length_str = len(s)
    count = s.count('a')

    cociente = n // length_str
    residuo = int(n % length_str)

    total = cociente * count
    total += s[:residuo].count('a')

    return(total)








if __name__ == '__main__':

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(result)