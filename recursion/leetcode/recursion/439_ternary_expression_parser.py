# https://leetcode.com/problems/ternary-expression-parser/description/?envType=problem-list-v2&envId=recursion&favoriteSlug=&difficulty=MEDIUM

"""
Given a string expression representing arbitrarily nested ternary expressions, evaluate the expression, and return the result of it.

You can always assume that the given expression is valid and only contains digits, '?', ':', 'T', and 'F' where 'T' is true and 'F' is false. All the numbers in the expression are one-digit numbers (i.e., in the range [0, 9]).

The conditional expressions group right-to-left (as usual in most languages), and the result of the expression will always evaluate to either a digit, 'T' or 'F'.
"""

class Solution:
    def parseTernary(self, expression):
        # recursive solution
        # since the expressions are nested, we need to find the nested expression and get ans for that
        # we can start from left to right, and we check whats the expression after ? and before corresponding :
        # important thing here is that we need to find corresponding : for that  ?
        # depending on condition is true or false, we recurse in specific direction

        def solve(i, j):
            # base condition when E1 or E2 is just 1 character and nothing to evaluate further
            if i == j:
                return expression[i]

            # get question index
            q_index = i
            while expression[q_index] != '?':
                q_index += 1

            # get corresponding after colon index
            afterColonIndex = q_index + 1
            count = 1
            while count != 0:
                if expression[afterColonIndex] == '?':
                    count += 1
                elif expression[afterColonIndex] == ':':
                    count -= 1
                afterColonIndex += 1

            # "T?T?F:5:3"
            #   |      |
            # q_idx   aft_col_idx
            # we want to recursively call for "T?F:5"
            # this is because expression is true

            if expression[i] == 'T':
                return solve(q_index + 1, afterColonIndex - 2)
            else:
                return solve(afterColonIndex, j)
        return solve(0, len(expression)-1)

    # iterative way
    # another way to solve this is to first evalaute the nested expression from right to left
    # so we identify the atomic expression from left and evaluate the same

    def prseTernary_iterative(self, expression):
        def isAtomic(s):
            if s[0] in 'TF' and s[1] == '?' and s[2] in 'TF0123456789' and s[3] == ':' and s[4] in 'TF0123456789':
                return True
            return False

        def evalExp(s):
            if s[0] == 'T':
                return s[2]
            return s[4]
        def solveAtomic(expression):
            i = len(expression)-1
            new_str = ""
            while i >= 0:
                new_str = expression[i] + new_str
                if len(new_str) == 5:
                    if isAtomic(new_str):
                        value = evalExp(new_str)
                        expression = expression[:i] + value + expression[i+5:]
                        return solveAtomic(expression)
                    else:
                        new_str = new_str[:-1]
                i -= 1
            return expression
        return solveAtomic(expression)

    # using stack
    def parseTernary_stack(self, expression):
        stack = []
        i = len(expression) - 1
        while i >= 0:
            if expression[i] != '?' and expression[i] != ':':
                stack.append(expression[i])
            else:
                if expression[i] == '?':
                    b = expression[i-1]
                    e1 = stack.pop()
                    e2 = stack.pop()
                    if b == 'T':
                        stack.append(e1)
                    else:
                        stack.append(e2)
                    i -= 1
            i -= 1
        return stack[-1]

a = Solution()
expression = "T?T?F:5:3"
print(a.parseTernary(expression))
print(a.prseTernary_iterative(expression))
print(a.parseTernary_stack(expression))