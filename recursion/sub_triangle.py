def subTriangle(arr):
    # base condition where we want to return
    if len(arr) == 1:
        print(arr)
        return

    # reduce array
    arr1 = [0]*(len(arr)-1)
    for i in range(len(arr)-1):
        arr1[i] = arr[i] + arr[i+1]
    # make a recursive call with reduced array size
    subTriangle(arr1)

    # printing at the end because when we make recursive call above, if we print before the output is going to
    # be in reverse direction
    print(arr)

arr = [1, 2, 3, 4, 5]
subTriangle(arr)