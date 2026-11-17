class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[0] * (n + 1) for _ in range(n)]

        for l in range(n):
            for r in range(l + 1, n):
                m = r - l + 1
                cost[l][r] = float('inf')

                for d in range(1, m):
                    if m % d == 0:
                        c = 0
                        for i in range(d):
                            a, b = l + i, r - (d - 1 - i)
                            while a < b:
                                c += s[a] != s[b]
                                a += d
                                b -= d
                        cost[l][r] = min(cost[l][r], c)

        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for j in range(1, k + 1):
            for i in range(2 * j, n + 1):
                for p in range(2 * (j - 1), i - 1):
                    dp[j][i] = min(dp[j][i], dp[j - 1][p] + cost[p][i - 1])

        return dp[k][n]