class TreeNode:
    def __int__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumSubTrees(self, root):
        nodeSum = {}
        def sumTree(root):
            if not root:
                return 0

            nodeSum[root] = sumTree(root.left) + sumTree(root.right) + root.val
            return nodeSum[root]

        sumTree(root)
