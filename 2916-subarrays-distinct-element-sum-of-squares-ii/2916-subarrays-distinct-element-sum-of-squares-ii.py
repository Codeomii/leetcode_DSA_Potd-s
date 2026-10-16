class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        size = 1
        while size < n:
            size *= 2
        s = [0] * (2 * size)
        sq = [0] * (2 * size)
        lazy = [0] * (2 * size)

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                d = 1
                length = r - l + 1
                sq[node] = (sq[node] + 2 * s[node] * d + length * d * d) % MOD
                s[node] = (s[node] + length * d) % MOD
                lazy[node] += d
                return
            mid = (l + r) // 2
            if lazy[node]:
                d = lazy[node]
                for child, a, b in ((node * 2, l, mid), (node * 2 + 1, mid + 1, r)):
                    length = b - a + 1
                    sq[child] = (sq[child] + 2 * s[child] * d + length * d * d) % MOD
                    s[child] = (s[child] + length * d) % MOD
                    lazy[child] += d
                lazy[node] = 0
            if ql <= mid:
                update(node * 2, l, mid, ql, qr)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr)
            s[node] = (s[node * 2] + s[node * 2 + 1]) % MOD
            sq[node] = (sq[node * 2] + sq[node * 2 + 1]) % MOD

        last = {}
        ans = 0
        for i, x in enumerate(nums):
            p = last.get(x, -1)
            update(1, 0, size - 1, p + 1, i)
            last[x] = i
            ans = (ans + sq[1]) % MOD
        return ans