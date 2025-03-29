# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/?envType=problem-list-v2&envId=binary-tree
"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
"""
class TreeNode(object):
    def __int__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root):
        def solve(root):
            if not root:
                return None

            if not root.left and not root.right:
                return root

            leftHead = solve(root.left)
            if leftHead:
                temp = leftHead
                while temp and temp.right:
                    temp = temp.right
                temp.right = root.right
                root.right = root.left
                root.left = None

            rightHead = solve(root.right)
            return rightHead if rightHead else leftHead
        

