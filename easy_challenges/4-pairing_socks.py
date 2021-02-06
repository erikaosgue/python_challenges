#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sock_seen = set()
    count_pairs = 0
    for sock in ar:
        if sock in sock_seen:
            count_pairs += 1
            sock_seen.remove(sock)
        else:
            sock_seen.add(sock)
    return(count_pairs)

if __name__ == '__main__':


    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
