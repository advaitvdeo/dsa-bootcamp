# https://leetcode.com/problems/reverse-nodes-in-k-group/description/?envType=problem-list-v2&envId=recursion&favoriteSlug=&difficulty=HARD

"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k):

        def reverseLL(curr, k):
            prev = None
            while k:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                k -= 1
            return prev

        def reverseKGroup(head, k):
            count = 0
            next_head = head
            while count < k and next_head:
                next_head = next_head.next
                count += 1

            if count == k:
                rev_head = reverseLL(head, k)
                head.next = reverseKGroup(next_head, k)
                return rev_head
            return head

    def reverseKGroup_iterative(self, head, k):

        def reverseLL(curr, k):
            prev = None
            while k:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                k -= 1
            return prev

        ptr = head
        new_head = None
        ktail = None
        while ptr:
            head = ptr
            count = 0
            while ptr and count < k:
                ptr = ptr.next
                count += 1

            if count == k:
                rev_head = reverseLL(head, k)
                if not new_head:
                    new_head = rev_head

                if ktail:
                    ktail.next = rev_head

                ktail = head
                head = ptr
        if ktail:
            ktail.next = head
        return new_haed