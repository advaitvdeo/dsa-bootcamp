import heapq
class Solution:
    def dijkstra(self, adj, V, source):
        min_heap = []
        result = [float('inf')] * V
        result[source] = 0
        heapq.heappush((0, source))

        while min_heap:
            dist, node = heapq.heappop(min_heap)
            for nei in adj[node]:
                wt, adjnode = nei[0], nei[1]
                if dist + wt < result[adjnode]:
                    result[adjnode] = dist + wt
                    heapq.heappush(min_heap, (dist + wt, adjnode))
        return result