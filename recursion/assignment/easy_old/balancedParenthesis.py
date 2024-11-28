def getClosing(bracket):
    if bracket == '(':
        return ')'
    if bracket == '[':
        return ']'
    if bracket == '{':
        return '}'
    return None

def balancedParenthesis(exp):
    n = len(exp)
    if n == 0:
        return True
    if n == 1:
        return False
    if exp[0] == ')' or exp[0] == ']' or exp[0] == '}':
        return False

    closing = getClosing(exp[0])
    i, count = 1, 0
    while i < n:
        if exp[i] == exp[0]:
            count += 1
        if exp[i] == closing:
            if count == 0:
                break
            count -= 1
        i += 1

    if i == n:
        return False

    if i == 2:
        return balancedParenthesis(exp[i:])

    return balancedParenthesis(exp[1:i]) and balancedParenthesis(exp[i+1:])


bracket = "[()]{}{[()()]()}"
#bracket = "[(])"
print(balancedParenthesis(bracket))