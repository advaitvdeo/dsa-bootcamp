class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def createBST(self, nums):
        def rightRotate(root):
            c = root.left
            t = c.right

            c.right = root
            root.left = t
            return c

        def leftRotate(root):
            p = root.right
            t = p.left

            p.left = root
            root.right = t
            return p

        def rotate(root):
            # left heavy case
            if self.height(root.left) - self.height(root.right) > 0:
                # left-left case
                if self.height(root.left.left) - self.height(root.left.right) > 0:
                    return rightRotate(root)
                # left-right case
                elif self.height(root.left.left) - self.height(root.left.right) < 0:
                    root.left = leftRotate(root.left)
                    return rightRotate(root)
            # right heavy case
            if self.height(root.right) - self.height(root.left) > 0:
                # right-right case
                if self.height(root.right.right) - self.height(root.right.left) > 0:
                    return leftRotate(root)
                # right-left case
                elif self.height(root.right.right) - self.height(root.right.left) < 0:
                    root.right = rightRotate(root.right)
                    return leftRotate(root)
            return root
        def insert(value, root):
            if not root:
                root = Node(value)
                return root
            if value > root.val:
                root.right = insert(value, root.right)
            else:
                root.left = insert(value, root.left)
            return rotate(root)

        root = None
        for i in range(len(nums)):
            root = insert(nums[i], root)
        return root

    def height(self, root):
        if not root:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))

    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.val, end='->')
            self.inorderTraversal(root.right)


nums = [4, 7, 8, 3, 5, 2, 9, 6, 1]
nums.sort()
a = Solution()
nums1 = []
for i in range(1, 1001):
    nums1.append(i)
root = a.createBST(nums1)
print(a.height(root))
a.inorderTraversal(root)