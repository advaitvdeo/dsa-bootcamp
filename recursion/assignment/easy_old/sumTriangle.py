def sumTriangle(arr):
    if len(arr) == 1:
        print(arr)
        return

    new_arr = []
    for i in range(len(arr)-1):
        new_arr.append(arr[i] + arr[i+1])
    sumTriangle(new_arr)

    print(arr)


arr = [1, 2, 3, 4, 5]
sumTriangle(arr)