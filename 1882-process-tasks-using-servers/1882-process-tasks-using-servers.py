import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []
        ans = []
        time = 0

        for i, d in enumerate(tasks):
            time = max(time, i)

            if not free and busy:
                time = max(time, busy[0][0])

            while busy and busy[0][0] <= time:
                _, w, idx = heapq.heappop(busy)
                heapq.heappush(free, (w, idx))

            w, idx = heapq.heappop(free)
            ans.append(idx)
            heapq.heappush(busy, (time + d, w, idx))

        return ans