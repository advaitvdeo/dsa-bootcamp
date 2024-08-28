# def bubbleSort(arr, swap):
#     if not swap:
#         return
#
#     swap = False
#     for i in range(len(arr)-1):
#         if arr[i] > arr[i+1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]
#             swap = True
#
#     bubbleSort(arr, swap)

# using single recursive call and a loop
def bubbleSort(n):
    if n == 1:
        return
    swap = False
    # using for loop
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            swap = True
    if not swap:
        return
    bubbleSort(n-1)


# using 2 recursive call
def bubbleSort2(arr, last, curr):
    if last == 0:
        return

    if curr < last:
        if arr[curr] > arr[curr+1]:
            arr[curr], arr[curr+1] = arr[curr+1], arr[curr]
        bubbleSort2(arr, last, curr+1)
    else:
        bubbleSort2(arr, last-1, 0)


arr = [2, 5, 4, 8, 1]
#bubbleSort(len(arr))
bubbleSort2(arr, len(arr)-1, 0)

print(arr)