from collections import deque

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
class Solution:
    def createTree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        root.left.left.left = Node(8)
        root.left.left.right = Node(9)
        root.left.right.left = Node(10)
        root.left.right.right = Node(11)
        root.right.left.left = Node(12)
        root.right.left.right = Node(13)
        root.right.right.left = Node(14)
        root.right.right.right = Node(15)

        return root


    def levelOrderTraversal(self, root):
        q = deque()
        q.append(root)
        ans = []
        while q:
            root = q.popleft()
            ans.append(root.val)
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
        return ans


nums = [4, 7, 8, 3, 5, 2, 9, 6, 1]
a = Solution()
root = a.createTree()
print(a.levelOrderTraversal(root))