#!/usr/bin/python3

import numpy

def numpy_array(arr):
    new_array = numpy.array(arr)
    return(numpy.reshape(new_array,(3,3)))


if __name__ == "__main__":
    array = list(map(int, input().split()))
    print(numpy_array(array))
