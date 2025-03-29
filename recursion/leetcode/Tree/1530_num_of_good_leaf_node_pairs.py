from collections import defaultdict, deque
class TreeNode:
    def __int__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root, distance):
        self.graph = defaultdict(list)
        self.leaf_nodes = []
        def traverse(root, parent):
            if not root:
                return None

            if not root.left and not root.right:
                self.leaf_nodes.append(root)

            if root:
                self.graph[root].append(parent)
            if parent:
                self.graph[parent].append(root)

            traverse(root.left, root)
            traverse(root.right, root)

        traverse(root, None)
        def solve(root):
            self.ans = 0
            for leaf in self.leaf_nodes:
                q = deque()
                seen = set()
                q.append(leaf)
                seen.add(leaf)
                for i in range(distance + 1):
                    curr_size = len(q)
                    for _ in range(curr_size):
                        node = q.popleft()
                        if node in self.leaf_nodes and node != leaf:
                            self.ans += 1
                        for nei in self.graph[node]:
                            if nei not in seen:
                                seen.add(nei)
                                q.append(nei)
        solve(root)
        return self.ans // 2
