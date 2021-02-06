#!/usr/bin/python3



def minTime(files, numCores, limit):
    # Write your code here
    parallel = []
    total_time = 0

    if numCores == 1:
        return sum(files)
    for i in files:
        print(" i, i % numCores",i,  i % numCores != 0)
        if i % numCores != 0:
            total_time += i
            print("added to sum ", i)
        if len(parallel) < limit:
            parallel.append(i)
            print("1", parallel)
        else:
            parallel.sort()
            print(parallel)
            if (parallel[0] >= i):
                total_time += i
                break
            else:
                parallel.pop(0)
                parallel.append(i)

    for i in parallel:
        print("@ i", parallel, i)
        total_time += i / numCores
    return int(total_time)


if __name__ == "__main__":
    files = [2, 3000, 2, 2, 2]
    # files = [2, 3000]
    # files = [2, 3000]
    numCores = 2
    limit = 3
    print("files: {}, numCores: {}, limit: {}".format(files, numCores, limit))
    print(minTime(files, numCores, limit))