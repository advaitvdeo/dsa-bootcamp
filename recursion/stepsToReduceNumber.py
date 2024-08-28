# pattern 1, where we don't pass 2nd argument (steps)
# In this pattern we just return the value that is computed outside of the function call
# return 1 + function_call

def stepsToReduceNumber(num):
    if num == 0:
        return 0

    if num % 2 != 0:
        return 1 + stepsToReduceNumber(num - 1)
    else:
        return 1 + stepsToReduceNumber(num // 2)


# in this pattern we pass 2nd argument of steps
# in this pattern we compute the values inside the function call
# return function_call(arg1, val + 1)

def stepsToReduceNumber2(num, steps):
    if num == 0:
        return steps

    if num % 2 == 0:
        return stepsToReduceNumber2(num/2, steps+1)
    return stepsToReduceNumber2(num-1, steps+1)

num = 123
print(stepsToReduceNumber(num))
print(stepsToReduceNumber2(num, 0))