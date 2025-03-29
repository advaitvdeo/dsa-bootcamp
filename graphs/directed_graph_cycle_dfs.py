from collections import defaultdict
class Solution:
    def detectCycle(self, edges, nodes):
        def dfs(u):
            if visited[u]:
                return True

            visited[u] = 1
            inRecursion[u] = 1

            for v in adj[u]:
                if not visited[v]:
                    if dfs(v):
                        return True
                elif inRecursion[v]:
                    return True

            inRecursion[u] = 0
            return False

        adj = defaultdict(list)
        for u, v_list in enumerate(edges):
            for v in v_list:
                adj[u].append(v)

        visited = [0]*nodes
        inRecursion = [0]*nodes

        for u in nodes:
            if not visited[u]:
                if dfs(u):
                    return True
        return False
