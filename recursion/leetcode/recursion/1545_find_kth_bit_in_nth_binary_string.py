# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/?envType=problem-list-v2&envId=recursion&favoriteSlug=&difficulty=MEDIUM

"""
Given two positive integers n and k, the binary string Sn is formed as follows:

S1 = "0"
Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first four strings in the above sequence are:

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

"""

class Solution:
    def findKthBit(self, n, k):
        # basic intuitive recursive approach
        def solve(index, n, k, string):
            if index >= n:
                return string

            new_str = ""
            for ch in string:
                if ch == "1":
                    new_str = '0' + new_str
                else:
                    new_str = '1' + new_str
            string += "1" + new_str

            return solve(index+1, n, k, string)
        return solve(1, n, k, "0")[k-1]

    def findKthBit_iterative(self, n, k):
        # using iterative approach
        string = '0'
        i = 1
        while i <= n:
            new_str = ""
            for ch in string:
                if ch == "1":
                    new_str = '0' + new_str
                else:
                    new_str = '1' + new_str
            string += "1" + new_str
            i += 1
        return string[k-1]

    def findKthBit_efficient_recursive(self, n, k):
        # we use the binary tree and elimination of sides when it comes to search
        if n == 1:
            return '0'

        last_row_nodes = 2**n
        if k < last_row_nodes//2:
            return self.findKthBit_efficient_recursive(n-1, k)
        elif k == last_row_nodes //2:
            return "1"
        else:
            corresponding_bit = self.findKthBit_efficient_recursive(n-1, last_row_nodes-k)
            return "1" if corresponding_bit == "0" else "0"


a = Solution()
n = 4
k = 11
print(a.findKthBit(n, k))
print(a.findKthBit_iterative(n, k))
print(a.findKthBit_efficient_recursive(n, k))