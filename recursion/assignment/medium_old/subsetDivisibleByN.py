def subsetDivisibleByN(arr, n, index, ds):
    if index >= len(arr):
        return 0

    ans = 0
    for i in range(index, n):
        if (sum(ds) + arr[i]) % n == 0:
            ans += 1 + subsetDivisibleByN(arr, n, i+1, ds + [arr[i]])
        ans += subsetDivisibleByN(arr, n, i+1, ds)
    return ans


arr = [4, 6, 12]
print(subsetDivisibleByN(arr, len(arr), 0, []))