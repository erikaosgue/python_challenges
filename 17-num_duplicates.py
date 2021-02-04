#!/usr/bin/python3

## Return an Int the amount of duplicates found
# have to have the same name, price and weights
def numDuplicates(names, prices, weights):
    # Write your code here
    
    uniq_dict = {}
    count = 0
    # values  = {}
    for i, name in enumerate(names):
       
        if name not in uniq_dict:
            uniq_dict[name]= [[prices[i], weights[i]]]
        else:
            list_val = uniq_dict[name]
            for l in  list_val:
                if l[0] == prices[i] and l[1] == weights[i]:
                    count += 1
                    break
            uniq_dict[name].append([prices[i], weights[i]])
            print(uniq_dict)
                    

    return count

if __name__ == '__main__':

    # list = [4
    #         EMPTY
    #         3
    #         5
    #         2
    #         3
    #         6
    #         1
    #         1
    #         4
    #         1
    #         8]

                #     4
                # EMPTY
                # 3
                # 5
                # 2
                # 3
                # 6
                # 1
                # 1
                # 4
                # 1
                # 8

    names = ['ball', 'box', 'ball', 'ball', 'box']
    prices = [2,2,2,2,2]
    weights = [1,2,1,1,3]
    print(numDuplicates(names, prices, weights))