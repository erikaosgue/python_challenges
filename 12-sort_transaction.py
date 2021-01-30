#!/usr/bin/python3


def transactions(array):
    # get the name and the number of time that apper
    # sort for the biggest amount of the same word

    dict_names = {}
    for name in array:
        if name not in dict_names:
            dict_names[name] = 0
        dict_names[name] += 1
    
    sorted_tuple = []
    for k, v in dict_names.items():
        sorted_tuple.append((k, v))
    sorted_list = sorted(sorted_tuple, key=lambda item: (item[0]))
    l = sorted(sorted_list, key=lambda item: item[1], reverse=True)
    new_list = []
    
    for k, v in l:
        new_list.append(k + " " +  str(v))
    return(new_list)





if __name__ == "__main__":
    array = ['Peter', 'Carlos', 'Sebastian', 'Peter', 'Peter', 'Carlos', 'Carlos', 'Zio', 'Zio', 'Zio', 'Zio']
    print(transactions(array))