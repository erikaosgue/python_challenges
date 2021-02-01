#!/usr/bin/python3

def hourglassSum(arr):
    
    max_value = -9 * 7
    value = 0
    for i in range(0, 4):
        for j in range(0, 4):
            value += arr[i][j] + arr[i][j+1] + arr[i][j+2]
            value += arr[i+1][j+1]
            value += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            print("3", value)

            if max_value <= value:
                max_value = value
            value = 0
    return(max_value)

if __name__ == '__main__':
    # arr = [
    #         [1, 1, 1, 0, 0, 0],
    #         [0, 1, 0, 0, 0, 0],
    #         [1, 1, 1, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0]
    #     ]

    arr = [
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0]
        ]


    # arr = [
    #         [-9, -9, -9,  1, 1, 1], 
    #         [0, -9,  0,  4, 3, 2],
    #         [-9, -9, -9,  1, 2, 3],
    #         [0,  0,  8,  6, 6, 0],
    #         [0,  0,  0, -2, 0, 0],
    #         [0,  0,  1,  2, 4, 0]
    # ]
    print(hourglassSum(arr))