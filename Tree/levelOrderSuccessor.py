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

    def levelOrderSuccessor(self, root, value):
        q = deque()
        q.append(root)
        ans = -1
        while q:
            root = q.popleft()
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
            if root.val == value:
                ans = q.popleft()
                break
        return ans.val

a = Solution()
root = a.createTree()
print(a.levelOrderSuccessor(root, 11))