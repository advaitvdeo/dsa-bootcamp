# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/description/?envType=problem-list-v2&envId=backtracking&difficulty=MEDIUM

"""
Given an integer n, find a sequence that satisfies all of the following:

The integer 1 occurs once in the sequence.
Each integer between 2 and n occurs twice in the sequence.
For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.
"""

class Solution:
    def constructDistancedSequence(self, n):
        ans = [-1] * (2*n-1)
        def solve(index, visited):
            if len(visited) == n or index >= 2*n-1:
                return True

            if ans[index] != -1:
                return solve(index+1, visited)

            for i in range(n, 0, -1):
                if i in visited:
                    continue

                if i+index >= 2*n-1 and i != 1:
                    continue

                if i != 1 and ans[i+index] != -1:
                    continue

                visited.add(i)
                ans[index] = i
                if i != 1:
                    ans[i+index] = i

                if solve(index+1, visited):
                    return True

                if i != 1:
                    ans[i + index] = -1
                visited.remove(i)
                ans[index] = -1

            return False
        solve(0, set())
        return ans


a = Solution()
n = 3
print(a.constructDistancedSequence(n))

