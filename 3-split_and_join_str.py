#!/usr/bin/python3

def split_and_join(line):
    line = "-".join(line.split(" "))
    return line 

if __name__ == "__main__":
    print(split_and_join("this is a string"))