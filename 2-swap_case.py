#!/usr/bin/python3

""" Given a string Swap cases
This version takes more time, because is creatin """

def swap_case(s):
    new_string =  "".join(char.lower() if char.isupper() else char.upper()  for char in s)
    return(new_string)

if __name__ == '__main__':
    s = input()
    # s = "ErIkA OsOrIo"
    result = swap_case(s)
    print(result)