class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def createTree(self, start, end, nums):
        if start > end:
            return None

        mid = start + (end-start)//2
        root = Node(nums[mid])
        root.left = self.createTree(start, mid-1, nums)
        root.right = self.createTree(mid+1, end, nums)

        return root

    def createBST(self, value, root):
        if not root:
            root = Node(value)
            return root
        if value > root.val:
            root.right = self.createBST(value, root.right)
        else:
            root.left = self.createBST(value, root.left)
        return root

    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.val, end='->')
            self.inorderTraversal(root.right)

    def createBSTTree(self, nums):
        root = None
        for i in range(len(nums)):
            root = self.createBST(nums[i], root)
        return root

nums = [4, 7, 8, 3, 5, 2, 9, 6, 1]
a = Solution()
root = a.createTree(0, len(nums)-1, nums)
a.inorderTraversal(root)
print("\n")

root = a.createBSTTree(nums)
a.inorderTraversal(root)