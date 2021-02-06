#!/usr/bin/python3

def get_decimal_number(roman_num):
    map_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'None': 0}
    other_val = {9, 4, 40}

    # check when only there is one char
    if roman_num in map_values:
        return(map_values[roman_num])

    decimal_num = 0
    
    if (len(roman_num) < 2):
        return

    last = roman_num[0]
    for i in range(1, len(roman_num)):
        curr = roman_num[i]
        
        total_sub = map_values[curr] - map_values[last]
        if total_sub % 10 in other_val or total_sub in other_val:
            decimal_num += total_sub
            last = "None"
            continue

        elif i == len(roman_num) - 1:
            decimal_num += map_values[curr]
            decimal_num += map_values[last]
        
        else:
            decimal_num += map_values[last]

        last = curr
        
    return decimal_num

def sort_roman_numbers(names):
    # Sort first by name
    # then sort by number
    new_list = []
    for element in names:
        name, roman_num = element.split(" ")
        decimal_num = get_decimal_number(roman_num)
        new_list.append((name, decimal_num, roman_num))
    x = sorted(new_list, key=lambda item: (item[0], item[1]))
    l = [name + " " + roman_num for name, _, roman_num, in x]
    return l




if __name__ == "__main__":

    names = ['Juan X', 'Sebastian XL', 'Cristian III', 'Julio IV', 'Juan XII']
    # names = ['Steven XL', 'Steven XVI', 'David IX', 'Mary XV', 'Masy XIII', 'Mary XX', 'Erika XLIV', 'Leon XLIX']
    print(sort_roman_numbers(names))