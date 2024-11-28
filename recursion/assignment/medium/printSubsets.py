def printSubsets(arr, ds, index):
    if ds:
        print(ds)

    for i in range(index, len(arr)):
        printSubsets(arr, ds + [arr[i]], i+1)


arr = [1, 2, 3]
printSubsets(arr, [] , 0)