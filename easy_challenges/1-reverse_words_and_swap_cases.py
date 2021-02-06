#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):

    sentence = list(sentence)

    sentence = list(sentence)
    last_idx = len(sentence) -1
    start_idx = 0
    
    
    while start_idx < last_idx:
        sentence[start_idx], sentence[last_idx] = sentence[last_idx], sentence[start_idx]
        start_idx += 1
        last_idx -= 1
        
    start_word = 0
    for i, char in enumerate(sentence):
        last_char = i - 1
        if char == " " or i == len(sentence) - 1:
            if i == len(sentence) - 1:
                last_char = i

            while start_word < last_char:
                sentence[start_word], sentence[last_char] = sentence[last_char], sentence[start_word]
                start_word += 1
                last_char -= 1
            start_word = i + 1
    
    for i, char in enumerate(sentence):
        if char.islower():
            sentence[i] = char.capitalize()

        else:
            sentence[i] = char.lower()
    string = "".join(sentence)
    return(string)

if __name__ == '__main__':
 
    sentence = "aWESOME is cODING"

    result = reverse_words_order_and_swap_cases(sentence)

    print(result)