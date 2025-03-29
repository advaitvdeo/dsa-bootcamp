class ListNode(object):
    def __int__(self, value):
        self.val = value
        self.next = None

class TreeNode(object):
    def __int__(self, value, left=None, right=None):
        self.val = value
        self.left = None
        self.right = None

class solution:
    def sortedListToBST_sol1(self, head):
        # in this solution, we convert into an array and we create BST
        self.arr = []
        node = head
        while node:
            self.arr.append(node.val)
            node = node.next

        def solve(start, end):
            if start > end:
                return None

            if start == end:
                return TreeNode(self.arr[start])

            mid = (start + end) // 2
            root = TreeNode(self.arr[mid])
            root.left = solve(start, mid-1)
            root.right = solve(mid+1, end)

            return root
        return solve(0, len(self.arr)-1)

    def sortedListToBST_sol1(self, head):
        # in this option we don't convert this into a array
        # instead we directly use linked list to create BST

        def getMid(node):
            slow = node
            fast = node
            prev = None
            while node and node.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev:
                prev.next = None
            return slow

        def solve(head):
            if not head:
                return None

            mid = getMid(head)
            root = TreeNode(mid.val)
            if mid == head:
                return root
            root.left = solve(head)
            root.right = solve(mid.next)

            return root
        return solve(head)

