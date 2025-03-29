from collections import defaultdict, deque
class Solution:
    def travel(self, edges, nodes):
        def bfs(u):
            q = deque()
            q.append(u)
            visited.add(u)
            result = [u]
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if v not in visited:
                        result.append(v)
                        visited.add(v)
                        q.append(v)
            return result

        adj = defaultdict(list)
        for u, v_list in enumerate(edges):
            for v in v_list:
                adj[u].append(v)

        visited = set()
        return bfs(0)


nodes = 5
edges = [[2, 3, 1], [0], [0, 4], [0], [2]]
a = Solution()
res = a.travel(edges, nodes)
print(res)