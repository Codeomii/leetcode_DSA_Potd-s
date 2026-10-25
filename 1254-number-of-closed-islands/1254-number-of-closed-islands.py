class Solution:
    def closedIsland(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if grid[i][j] == 1:
                return 1

            grid[i][j] = 1
            a = dfs(i + 1, j)
            b = dfs(i - 1, j)
            c = dfs(i, j + 1)
            d = dfs(i, j - 1)
            return a & b & c & d

        ans = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    ans += dfs(i, j)

        return ans