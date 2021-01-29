#!/usr/bin/python3

def is_leap(year):
    leap = False

    # leap year have to be divided by 4 and not by 100, or
    # leap year have to be divided by 400
    
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap = True
    
    
    return leap


if __name__ == "__main__":
    year = int(input())
    print(is_leap(year))