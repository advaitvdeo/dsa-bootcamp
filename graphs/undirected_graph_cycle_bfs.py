from collections import defaultdict, deque
class Solution:
    def detectCycle(self, edges, nodes):

        def bfs(u):
            q = deque()
            q.append((u, -1))
            while q:
                u, parent = q.popleft()
                visited[u] = 1
                for v in adj[u]:
                    if not visited[v]:
                        q.append((v, u))
                    elif v != parent:
                        return True
            return False

        adj = defaultdict(list)
        for u, v_list in enumerate(edges):
            for v in v_list:
                adj[u].append(v)

        visited = [0]*nodes
        for u in range(nodes):
            if not visited[u]:
                if bfs(u):
                    return True
        return False


nodes = 4
#edges = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
edges = [[], [2], [1, 3], [2]]
a = Solution()
result = a.detectCycle(edges, nodes)
print(result)