from collections import defaultdict
class Solution:
    def travel(self, edges, nodes):
        def dfs(u):
            if u in visited:
                return

            visited.add(u)
            result.append(u)
            for v in adj[u]:
                if v not in visited:
                    dfs(v)

        result = []
        visited = set()
        adj = defaultdict(list)
        for u, v_list in enumerate(edges):
            for v in v_list:
                adj[u].append(v)

        for u in range(nodes):
            if u not in visited:
                dfs(u)
        return result


nodes = 5
edges = [[2, 3, 1], [0], [0, 4], [0], [2]]
a = Solution()
result = a.travel(edges, nodes)
print(result)
