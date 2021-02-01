#!/usr/bin/python3


def transactions(array):
    # get the name and the number of time that apper
    # sort for the biggest amount of the same word

    dict_names = {}
    for name in array:
        if name not in dict_names:
            dict_names[name] = 0
        dict_names[name] += 1
    
    unsorted_tuple = []
    for k, v in dict_names.items():
        unsorted_tuple.append((k, v))
    # First sort by name
    sorted_list_by_name = sorted(unsorted_tuple, key=lambda item: (item[0]))
    # then sort by value which is sum of the repeated names
    sorted_by_greates_value = sorted(sorted_list_by_name, key=lambda item: item[1], reverse=True)
    
    # Transform a list of tuples to a list of the form ['name quantity']
    new_list = []    
    for k, v in sorted_by_greates_value:
        new_list.append(k + " " +  str(v))
    return(new_list)





if __name__ == "__main__":
    array = ['Dog', 'Cat', 'Bird', 'Snake', 'Dog', 'Snake', 'Snake', 'Bird']
    # array = ['Peter', 'Carlos', 'Sebastian', 'Peter', 'Peter', 'Carlos', 'Carlos', 'Zio', 'Zio', 'Zio', 'Zio']
    print(transactions(array))