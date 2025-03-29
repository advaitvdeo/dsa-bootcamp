# https://www.geeksforgeeks.org/problems/flatten-bst-to-sorted-list--111950/1
class TreeNode(object):
    def __int__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # https://www.youtube.com/watch?v=NzXtnzQTouk
    def flattenBST(self, root):
        if not root:
            return None

        head = self.flattenBST(root.left)
        root.left = None
        if head:
            temp = head
            while temp and temp.right:
                temp = temp.right
            temp.right = root
        else:
            head = root

        root.right = self.flattenBST(root.right)
        return head

