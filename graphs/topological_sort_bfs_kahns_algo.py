from collections import defaultdict, deque
class Solution:
    def topoSort(self, edges, nodes):

        # step 0: create adj list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        # step 1: create inDegree array
        inDegree = [0] * nodes
        for u in nodes:
            for v in adj[u]:
                inDegree[v] += 1

        # step 2: add nodes with indegree 0 to queue
        q = deque()
        for u in range(nodes):
            if inDegree[u] == 0:
                q.append(u)

        # step 3: iterate through queue and reduce indegree of nodes
        result = []
        while q:
            u = q.popleft()
            result.append(u)
            for v in adj[u]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    q.append(v)
        return result

