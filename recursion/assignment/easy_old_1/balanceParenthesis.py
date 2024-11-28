def getClosing(ch):
    if ch == '(':
        return ')'
    if ch == '[':
        return ']'
    if ch == '{':
        return '}'
    return None

def balanceParenthesis(exp):
    n = len(exp)
    if n == 0:
        return True
    if n == 1:
        return False
    if exp[0] == '}' or exp[0] == ']' or exp[0] == ")":
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
        return balanceParenthesis(exp[i:])

    return balanceParenthesis(exp[1:i]) and balanceParenthesis(exp[i+1:])


bracket = "[()]{}{[()()]()}"
#bracket = "[(])"
bracket = "(())"
print(balanceParenthesis(bracket))