class TreeNode:
    def __int__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root):
        self.last = None
        self.first = None
        def solve(root):
            if not root:
                return None

            solve(root.left)
            if self.last:
                self.last.right = root
                root.left = self.last
            else:
                self.first = root
            self.last = root

            solve(root.right)
        solve(root)
        self.first.left = self.last
        self.last.right = self.first
        return self.first
