from collections import defaultdict, deque
class Solution:
    def detectCycle(self, edges, nodes):
        # step 0: adj list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        # step 1: create indegree array
        inDegree = [0]*(nodes)
        for u in nodes:
            for v in adj[u]:
                inDegree[v] += 1

        # step 2: add nodes with 0 indegree to q
        count = 0
        q = deque()
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                q.append(inDegree[i])
                count += 1

        # Step 3: iterate through q
        while q:
            u = q.popleft()
            for v in adj[u]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    q.append(v)
                    count += 1

        return not (count == nodes)

