# https://leetcode.com/problems/k-th-symbol-in-grammar/?envType=problem-list-v2&envId=recursion&favoriteSlug=&difficulty=MEDIUM
"""
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows
"""
class Solution:
    def kthGrammar(self, n, k):
        # we need to visualize this as binary tree
        def solve(n, k, rootVal):
            if n == 1:
                return rootVal

            lastRowNodes = 2**(n-1)
            if k > lastRowNodes:
                rootVal = 1 if rootVal == 0 else 0
                return solve(n//2, k - (lastRowNodes//2), rootVal)
            else:
                return solve(n//2, k, rootVal)
        return solve(n, k, 0)


a = Solution()
n = 30
k = 123123
print(a.kthGrammar(n, k))