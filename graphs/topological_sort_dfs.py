from collections import defaultdict
class Solution:
    def topoSort(self, edges, nodes):
        def dfs(u):
            if visited[u]:
                return

            visited[u] = 1
            for v in adj[u]:
                if not visited[v]:
                    dfs(v)
            stack.append(u)

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        visited = [0]*nodes
        stack = []
        for u in nodes:
            if not visited[u]:
                dfs(u)

        res = []
        while stack:
            res.append(stack.pop())
        return res

