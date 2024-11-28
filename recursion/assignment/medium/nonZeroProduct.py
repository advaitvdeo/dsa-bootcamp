def nonZeroProduct(p):
    return (2**p-2)**((2**p-2)//2) * (2**p-1)

p = 3
print(nonZeroProduct(p))