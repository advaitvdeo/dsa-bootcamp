def gico(n, one, two, three):
    if n == 1:
        return one
    if n == 2:
        return two
    if n == 3:
        return three

    return gico(n-1, one, two, three) + gico(n-2, one, two, three) + gico(n-3, one, two, three)


one = 1
two = 2
three = 3

print(gico(4, one, two, three))