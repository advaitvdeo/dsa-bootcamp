class Node:
    def __init__(self, value, start, end):
        self.val = value
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class Solution:
    def createSegmentTree(self, nums):
        def constructTree(start, end):
            # leaf node
            if start == end:
                return Node(nums[start], start, end)

            root = Node(0, start, end)

            mid = (start + end)//2
            root.left = constructTree(start, mid)
            root.right = constructTree(mid+1, end)

            root.val = root.left.val + root.right.val

            return root
        return constructTree(0, len(nums)-1)

    def display(self, root):
        string = ""
        if root.left:
            string += "Interval=[" + str(root.left.start) + '-' + str(root.left.end) + "] and data: " + str(root.left.val) + "=>"
        else:
            string += "No left child"

        string += "Interval=[" + str(root.start) + '-' + str(root.end) + "] and data: " + str(root.val) + "=>"

        if root.right:
            string += "Interval=[" + str(root.right.start) + '-' + str(root.right.end) + "] and data: " + str(root.right.val)
        else:
            string += "No right child"

        print(string + "\n")

        if root.left:
            self.display(root.left)
        if root.right:
            self.display(root.right)


    def query(self, root, qsi, qei):
        def solve(root, qsi, qei):
            if root.start >= qsi and root.end <= qei:
                # node is completely inside the range
                return root.val
            elif root.start > qei or root.end < qsi:
                return 0
            else:
                #overlap
                return solve(root.left, qsi, qei) + solve(root.right, qsi, qei)
        return solve(root, qsi, qei)

    def update(self, root, index, value):
        def solve(root, index, value):
            if index >= root.start and index <= root.end:
                if index == root.start and index == root.end:
                    root.val = value
                    return root.val
                else:
                    leftAns = solve(root.left, index, value)
                    rightAns = solve(root.right, index, value)
                    root.val = leftAns + rightAns
                    return root.val
            return root.val
        root.val = solve(root, index, value)



nums = [3, 8, 6, 7, -2, -8, 4, 9]
a = Solution()
root = a.createSegmentTree(nums)
print(a.query(root, 1, 6))
