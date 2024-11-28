# https://leetcode.com/problems/design-hashset/?envType=problem-list-v2&envId=linked-list&difficulty=EASY
# create hashset


# classical way to implement hash set is via the buckets
# we decide the hash function and number of buckets we need
# this is similar to how oracle managed the blocks in memory
# we then generate the hash of the value and look for the bucket to which it belongs
# once we know the bucket, we traverse the bucket to store or retrive the value

# in this case, we can use array to store the bucket location
# bucket itself would be linked list

class Node:
    def __int__(self, val, next=None):
        self.val = val
        self.next = next


# defining bucket class
class Bucket:
    def __int__(self):
        # sentinal node
        self.head = Node(0)

    def exists(self, val):
        curr = self.head.next
        while curr:
            if curr.val == val:
                return True
            curr = curr.next
        return False

    def insert(self, val):
        if not self.exists(val):
            new_node = Node(val, self.head.next)
            self.head.next = new_node

    def delete(self, val):
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.val == val:
                prev = curr.next
                return
            prev = curr
            curr = curr.next


class MyHashSet(object):
    def __init__(self):
        self.bucketRange = 769
        self.bucketArray = [Bucket() for _ in range(self.bucketRange)]

    def add(self, key):
        self.bucketArray[key % self.bucketRange].insert(key)
    def remove(self, key):
        self.bucketArray[key % self.bucketRange].delete(key)
    def contains(self, key):
        return self.bucketArray[key % self.bucketRange].exists(key)