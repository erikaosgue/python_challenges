#!/usr/bin/python3

# Print the number that is found on top of the stack everytime the is a new stack
def superStack(operations):
    arr = []
    
    for oper in operations:
        val = oper.split(" ")
        if len(val) == 1 and val[0] ==  'pop':
            arr.pop()
            if len(arr) > 0:
                print(arr[-1])
            else:
                print('EMPTY')
        elif len(val) == 2 and val[0] == 'push':
            arr.append(int(val[1]))
            print(arr[-1])
        elif len(val) == 3 and val[0] == 'inc':
            for i in range(int(val[1])):
                # print("arr", arr)
                arr[i] += int(val[2])
            print("==>", arr[-1])
            


if __name__ == "__main__":

    operations = [
        'push 4',
        'pop', 
        'push 3', 
        'push 5', 
        'push 2', 
        'inc 3 1', 
        'pop', 
        'push 1', 
        'inc 2 2', 
        'push 4', 
        'pop', 
        'pop']

    superStack(operations)