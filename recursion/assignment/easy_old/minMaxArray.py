def minMaxArray(arr, minVal, maxVal):
    if not arr:
        return minVal, maxVal

    minVal = min(minVal, arr[0])
    maxVal = max(maxVal, arr[0])

    return minMaxArray(arr[1:], minVal, maxVal)


arr = [1, 4, 3, -5, -4, 8, 6]
print(minMaxArray(arr, float('inf'), float('-inf')))