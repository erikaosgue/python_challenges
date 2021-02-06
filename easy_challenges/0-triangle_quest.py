#!/usr/bin/python3

if __name__ == "__main__":
    for i in range(1,int(input())):
        print(int(i * (10**i -1) /9))