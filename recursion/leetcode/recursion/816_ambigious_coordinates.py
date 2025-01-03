# https://leetcode.com/problems/ambiguous-coordinates/?envType=problem-list-v2&envId=backtracking&difficulty=MEDIUM
"""
We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)". Then, we removed all commas, decimal points, and spaces and ended up with the string s.

For example, "(1, 3)" becomes s = "(13)" and "(2, 0.5)" becomes s = "(205)".
Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with fewer digits. Also, a decimal point within a number never occurs without at least one digit occurring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order. All coordinates in the final answer have exactly one space between them (occurring after the comma.)
"""
class Solution:
    def ambiguousCoordinates(self, s):
        s = s.strip('(').strip(')')
        def generate(s):
            if len(s) == 1: return [s]
            if s[0] == '0' and s[-1] == '0': return []
            if s[0] == '0': return [s[:1] + '.' + s[1:]]
            if s[-1] == '0': return [s]
            return [s[:i] + '.' + s[i:] for i in range(1, len(s))] + [s]

        ans = []
        for i in range(1, len(s)):
            for x in generate(s[:i]):
                for y in generate(s[i:]):
                    ans.append("(%s, %s)"%(x, y))
        return ans


a = Solution()
s = "(123)"
print(a.ambiguousCoordinates(s))