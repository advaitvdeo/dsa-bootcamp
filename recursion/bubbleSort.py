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

def bubbleSort(n):
    if n == 1:
        return
    swap = False
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            swap = True
    if not swap:
        return
    bubbleSort(n-1)


arr = [5, 1, 4, 2, 8]
bubbleSort(len(arr))

print(arr)