class Solution:
    def shortestPath(self, n, edges, labels, k):
        import heapq

        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))

        pq = [(0, 0, 1)]
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0

        while pq:
            d, u, cnt = heapq.heappop(pq)

            if d != dist[u][cnt]:
                continue

            if u == n - 1:
                return d

            for v, w in g[u]:
                c = cnt + 1 if labels[u] == labels[v] else 1

                if c <= k and d + w < dist[v][c]:
                    dist[v][c] = d + w
                    heapq.heappush(pq, (d + w, v, c))

        return -1