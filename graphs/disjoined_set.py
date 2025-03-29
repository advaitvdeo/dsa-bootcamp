class Solution:
    def dsu(self, V):
        parent = [0]*V
        rank = [1]*V
        for i in range(V):
            parent[i] = i

        def find(x):
            if x == parent[x]:
                return x

            parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            parent_u = find(u)
            parent_v = find(v)

            if parent_u == parent_v:
                return

            if rank[parent_u] > rank[parent_v]:
                parent[parent_v] = parent_u
            elif rank[parent_u] < rank[parent_v]:
                parent[parent_u] = parent_v
            else:
                parent[parent_v] = parent_u
                rank[parent_u] += 1

