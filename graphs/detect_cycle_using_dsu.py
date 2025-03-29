from collections import defaultdict
class Solution:
    def detectCycle(self, graph, V):
        adj = defaultdict(list)
        for u, v in graph:
            adj[u].append(v)
            adj[v].append(u)

        parent = [0]*V
        rank = [0]*V
        for i in range(V):
            parent[i] = i
            rank[i] = 1

        def find(x):
            if x == parent[x]:
                return x

            parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            parent_u = find(u)
            parent_v = find(v)

            if parent_u == parent_v:
                return True

            if rank[parent_u] > rank[parent_v]:
                parent[parent_v] = parent_u
            elif rank[parent_u] < rank[parent_v]:
                parent[parent_u] = parent_v
            else:
                parent[parent_v] = parent_u
                rank[parent_u] += 1

        for u in range(V):
            for v in adj[u]:
                if u < v:
                    parent_u = find(u)
                    parent_v = find(v)
                    if parent_u == parent_v:
                        return True
                    union(u, v)
        return False
