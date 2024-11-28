# range of numbers = [1, 2**(p-1)]
# if p == 3, range of numbers = [1, 2, 3, 4, 5, 6, 7]
# [001, 010, 011, 100, 101, 110, 111]
# 001
# 010
# 011
# 100
# 101
# 110
# 111
# We can see that number of 1's and 0's at each place is same (unit place, tens place, hundreds place)
# Skipping last element, because we skipped 0

# 001 - 1
# 010 - 2
# 011
# 100
# 101 - 5
# 110 - 6

# if we bring 2 and 5 closer we can convert that into 1 and 6
# 010 - 2
# 101 - 4
# we can swap 2nd and 3rd elements
# 001 - 1
# 110 - 6

# similarly if we can bring 3 and 4 together, we can convert that into 2 and 5 and then 1 and 6
# 011 - 3
# 100 - 4
# swap middle bit
# 001 - 1
# 110 - 6

# like this we can convert all numbers (except last) into 1 and 6 (2**p - 2)
# so we will have half the numbers as 1 and half the numbers as (2**p - 2)
# so final ans will be (2**p - 2)**((2**p - 2)//2) * (2**p-1)
def minNonZeroProduct(p):
    return (2**p - 2)**((2**p-2)//2)*(2**p-1)


p = 3
print(minNonZeroProduct(p))