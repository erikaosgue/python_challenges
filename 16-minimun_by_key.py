#!/usr/bin/python3

# As a part of this problem, we're going to build, piece-by-piece,
# the part of a relational database that can take a list of rows and
# sort them by multiple fields:

# i.e., the part that implements
#       ORDER BY name ASC, age DESC

# Step 1: we want to write a function that returns the record
#         with the smallest entry of a given key
#
#         Treat missing keys as 0

def min_by_key(arr, key):
    
    min_val = arr[0]
    for dict_ in records:
        if key in dict_ :
            if key in min_val:
                if dict_[key] < min_val[key]:
                    min_val = dict_
            
        elif min_val[key]  > 0 :
            min_val = dict_
        
    return min_val
        

records = [
    {'a': 1, 'b': 4},
    {'a': 3, 'b': 1},
    {'a': 2}, 
    {'a': -2, 'b': 2},
    {'b': 3}
]

print('min_by_key')
print(min_by_key(records, 'a')) # -> {a: -2, b: 2}
print(min_by_key(records, 'b')) # -> {a: 2}, since we treat b as 0
