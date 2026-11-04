class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        import heapq

        n = len(nums)
        l, r = [], []
        ls = rs = 0
        delayed = {}
        lc = rc = 0
        costs = []

        def prune(h, sign):
            while h and delayed.get(sign * h[0], 0):
                v = sign * heapq.heappop(h)
                delayed[v] -= 1
                if not delayed[v]:
                    del delayed[v]

        def balance():
            nonlocal ls, rs, lc, rc
            while lc > rc + 1:
                prune(l, -1)
                v = -heapq.heappop(l)
                ls -= v
                lc -= 1
                heapq.heappush(r, v)
                rs += v
                rc += 1
            while lc < rc:
                prune(r, 1)
                v = heapq.heappop(r)
                rs -= v
                rc -= 1
                heapq.heappush(l, -v)
                ls += v
                lc += 1

        def add(v):
            nonlocal ls, rs, lc, rc
            prune(l, -1)
            if not l or v <= -l[0]:
                heapq.heappush(l, -v)
                ls += v
                lc += 1
            else:
                heapq.heappush(r, v)
                rs += v
                rc += 1
            balance()

        def remove(v):
            nonlocal ls, rs, lc, rc
            prune(l, -1)
            delayed[v] = delayed.get(v, 0) + 1
            if v <= -l[0]:
                ls -= v
                lc -= 1
                if v == -l[0]:
                    prune(l, -1)
            else:
                rs -= v
                rc -= 1
                if r and v == r[0]:
                    prune(r, 1)
            balance()

        for i, v in enumerate(nums):
            add(v)
            if i >= x:
                remove(nums[i-x])
            if i >= x-1:
                prune(l, -1)
                m = -l[0]
                costs.append(m*lc-ls + rs-m*rc)

        inf = float('inf')
        dp = [[inf]*(k+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 0

        for j in range(1, k+1):
            for i in range(x, n+1):
                dp[i][j] = min(
                    dp[i-1][j],
                    dp[i-x][j-1] + costs[i-x]
                )

        return dp[n][k]