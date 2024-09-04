def dice(arr, target, ds):
    if target == 0:
        print(ds)
        return
    if target < 0:
        return

    for i in range(len(arr)):
        if arr[i] <= target:
            dice(arr, target - arr[i], ds + [arr[i]])

def diceList(arr, target, ds):
    if target == 0:
        return [ds]
    if target < 0:
        return []

    ans = []
    for i in range(len(arr)):
        if arr[i] <= target:
            ans += diceList(arr, target-arr[i], ds + [arr[i]])

    return ans



arr = [1, 2, 3, 4, 5, 6]
target = 4
dice(arr, target, [])
print("-----------------------------")
print(diceList(arr, target, []))