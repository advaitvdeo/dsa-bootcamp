def findClosing(c):
    if c == '(': return ')'
    if c == '[': return ']'
    if c == '{': return '}'
def checkBalancedParenthesis(exp):
    # base condition
    n = len(exp)
    if n == 0:
        return True
    if n == 1:
        return False

    if exp[0] == ']' or exp[0] == ')' or exp[0] == '}':
        return False

    closing = findClosing(exp[0])
    i, count = 1, 0
    while i < n:
        if exp[i] == exp[0]:
            count += 1
        if exp[i] == closing:
            # this is in case closing bracket is next to opening one.
            # in this case, count will be 0 and since we found closing bracket
            # we can exit the loop and go for next recursive call for remaining expression
            if count == 0:
                break
            count -= 1
        i += 1

    # we did not find closing bracket
    if i == n:
        return False

    # closing bracket was next to open
    if i == 2:
        return checkBalancedParenthesis(exp[i:n-1])

    # this is first checking the outer brackets. if they match, we recursively call for inner brackets and remaining expression
    # after the outer bracket checks
    # first following is checked - [()]
    # then since [ and ] matched, it calls for () and {}{[()()]()}
    return checkBalancedParenthesis(exp[1:i]) and checkBalancedParenthesis(exp[i+1:n])



exp = "[()]{}{[()()]()}"
exp = "[(])"
print(checkBalancedParenthesis(exp))