def min_max_array(arr, start):
    # base condition
    if start == len(arr) - 1:
        return arr[start], arr[start]

    min_element, max_element = min_max_array(arr, start+1)
    min_return = min(arr[start], min_element)
    max_return = max(arr[start], max_element)
    # for i in range(start, len(arr)):
    #     if arr[i] < min_element:
    #         min_element = arr[i]
    #     if arr[i] > max_element:
    #         max_element = arr[i]
    return min_return, max_return


arr = [1, 4, 3, -5, -4, 8, 6]
min_element, max_element = min_max_array(arr, 0)
print(f"min element is {min_element}")
print(f"max element is {max_element}")