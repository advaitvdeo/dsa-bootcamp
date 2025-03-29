from collections import defaultdict
class Solution:
    def detectCycle(self, edges, nodes):
        adj = defaultdict(list)
        for u, v_list in enumerate(edges):
            for v in v_list:
                adj[u].append(v)

        visited = [0]*(nodes)
        result  = []
        def dfs(u, parent):
            if visited[u]:
                return

            visited[u] = 1
            result.append(u)
            for v in adj[u]:
                if v == parent:
                    continue
                if visited[v]:
                    return True
                if dfs(v, u):
                    return True

            return False

        for u in range(nodes):
            if not visited[u] and dfs(u, -1):
                return True
        return False


nodes = 5
edges = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
#edges = [[], [2], [1, 3], [2]]
a = Solution()
result = a.detectCycle(edges, nodes)
print(result)