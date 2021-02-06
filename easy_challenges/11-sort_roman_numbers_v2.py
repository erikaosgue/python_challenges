#!/usr/bin/python3



def transform_decimal_num(roman_num):
    
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'None': 0}

    if roman_num in roman_numbers:
        return roman_numbers[roman_num]

    i = 0
    sum_dec = 0
    while i <= len(roman_num) - 2:
        curr = roman_num[i]
        next_ = roman_num[i+1]
        if curr == 'I' and next_ == 'V':
            i += 1
            sum_dec += 4
        elif curr == 'I' and next_ == 'X':
            sum_dec += 9
            i += 1
        elif curr == 'X' and next_ == 'L':
            sum_dec += 40
            i += 1
        else:
            sum_dec += roman_numbers[curr]
            if i == len(roman_num) - 2:
                sum_dec += roman_numbers[next_]
            i += 1
    return sum_dec


def sortRoman(names):
    list_tuples = []
    for name in names:
        nam, roman_num = name.split(" ")
        dec_num = transform_decimal_num(roman_num)
        
        list_tuples.append((nam, roman_num, dec_num))
    list_tuples.sort(key=lambda tup: (tup[0], tup[2]))

    sorted_list = []
    print(list_tuples)
    for tup in list_tuples:
        sorted_list.append(tup[0] + " " + str(tup[1]))
    return (sorted_list)
    
if __name__ == '__main__':
    # names = ['Juan X', 'Sebastian XL', 'Cristian III', 'Julio IV', 'Juan XII']

    names = ['Louis IX', 'Louis VIII']
    print(sortRoman(names))