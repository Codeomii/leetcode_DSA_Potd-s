class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        s = nums + [0]
        N = n + 1

        p = sorted(range(N), key=lambda i: s[i])
        c = [0] * N

        for i in range(1, N):
            c[p[i]] = c[p[i-1]] + (s[p[i]] != s[p[i-1]])

        h = 0
        while (1 << h) < N:
            k = 1 << h
            pn = [(x - k) % N for x in p]

            cnt = [0] * N
            for x in pn:
                cnt[c[x]] += 1

            pos = [0] * N
            for i in range(1, N):
                pos[i] = pos[i-1] + cnt[i-1]

            np = [0] * N
            for x in pn:
                cl = c[x]
                np[pos[cl]] = x
                pos[cl] += 1

            p = np
            nc = [0] * N
            classes = 1

            for i in range(1, N):
                a, b = p[i], p[i-1]
                if (c[a], c[(a+k) % N]) != (c[b], c[(b+k) % N]):
                    classes += 1
                nc[a] = classes - 1

            c = nc
            h += 1

        sa = p[1:]
        rank = [0] * n

        for i, x in enumerate(sa):
            rank[x] = i

        lcp = [0] * (n - 1)
        k = 0

        for i in range(n):
            r = rank[i]

            if r == n - 1:
                k = 0
                continue

            j = sa[r + 1]

            while i + k < n and j + k < n and nums[i+k] == nums[j+k]:
                k += 1

            lcp[r] = k

            if k:
                k -= 1

        ans = n

        for r in range(n):
            length = max(
                lcp[r-1] if r > 0 else 0,
                lcp[r] if r < n-1 else 0
            ) + 1

            if length <= n - sa[r]:
                ans = min(ans, length)

        return ans