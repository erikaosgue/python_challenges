#!/usr/bin/python3


def transactions(array):
    # get the name and the number of time that apper
    # sort for the biggest amount of the same word

    dict_names = {}
    for name in array:
        if (name not in dict_names):
            dict_names[name] = 1
        else:
            dict_names[name] += 1
    sorted_list = []
    for k, v in dict_names.items():
        sorted_list.append(k + " " + str(v))
    x = sorted(sorted_list, key=lambda item: item.split(" ")[1], reverse=True)
    return(x)





if __name__ == "__main__":
    array = ['Peter', 'Carlos', 'Sebastian', 'Peter', 'Peter', 'Carlos', 'Zio', 'Zio', 'Zio', 'Zio']
    print(transactions(array))