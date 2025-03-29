# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/?envType=problem-list-v2&envId=binary-tree
class TreeNode(object):
    def __int__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, head):
        def findMid(head):
            slow = head
            fast = head
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev:
                prev.next = None
            return slow

        def solve(head):
            if not head:
                return None

            mid = findMid(head)
            root = TreeNode(mid.val)
            if head == mid:
                return root
            root.left = solve(head)
            root.right = solve(mid.next)

            return root
        return solve(head)