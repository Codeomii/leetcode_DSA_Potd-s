class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        h = [[0]*n for _ in range(m)]
        v = [[0]*n for _ in range(m)]
        h[0][0] = 1

        for i in range(m):
            for j in range(n):
                a, b = h[i][j], v[i][j]

                if grid[i][j]:
                    if a and i+1 < m:
                        v[i+1][j] = (v[i+1][j] + a) % MOD
                    if b and j+1 < n:
                        h[i][j+1] = (h[i][j+1] + b) % MOD
                else:
                    ways = (a+b) % MOD
                    if i == m-1 and j == n-1:
                        return ways
                    if j+1 < n:
                        h[i][j+1] = (h[i][j+1] + ways) % MOD
                    if i+1 < m:
                        v[i+1][j] = (v[i+1][j] + ways) % MOD

        return 0