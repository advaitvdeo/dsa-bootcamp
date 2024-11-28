def maxMinArray(arr, max_val, min_val):
    if len(arr) == 0:
        return max_val, min_val

    if max_val < arr[0]:
        max_val = arr[0]
    if min_val > arr[0]:
        min_val = arr[0]

    return maxMinArray(arr[1:], max_val, min_val)


arr = [1, 4, 45, 6, 10, -8]
print(maxMinArray(arr, float('-inf'), float('inf')))