class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        ht = {}
        for i, val in enumerate(inorder):
            ht[val] = i

        self.index = 0

        def solve(start, end):
            if start > end:
                return None

            val = preorder[self.index]
            root = TreeNode(val)
            self.index += 1
            i = ht[root.val]

            root.left = solve(start, i-1)
            root.right = solve(i+1, end)

            return root
        return solve(0, len(inorder)-1)


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

a = Solution()
print(a.buildTree(preorder, inorder))