def reverseString(str_arr, rev_arr, index):
    if index == len(str_arr) - 1:
        rev_arr.append(str_arr[index])
        return

    reverseString(str_arr, rev_arr, index+1)
    rev_arr.append(str_arr[index])


str_arr = ["h","e","l","l","o"]
rev_arr = []
reverseString(str_arr, rev_arr, 0)
print(rev_arr)