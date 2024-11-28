def divisibleSubset(arr, ds, index):
    if index >= len(arr):
        return 0

    count = 0
    for i in range(index, len(arr)):
        ds.append(arr[i])
        if sum(ds) % len(arr) == 0:
            count += 1
        count += divisibleSubset(arr, ds, i+1)
        ds.pop()

    return count


arr = [4, 6, 12]
print(divisibleSubset(arr, [], 0))