class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                if i:
                    dp[i][j].update(x ^ grid[i][j] for x in dp[i-1][j])
                if j:
                    dp[i][j].update(x ^ grid[i][j] for x in dp[i][j-1])

        return min(dp[-1][-1])