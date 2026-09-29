from functools import cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n) % 2 == 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        @cache
        def dfs(r: int, c: int, bal: int) -> bool:
            bal += 1 if grid[r][c] == '(' else -1
            if bal < 0 or bal > (m + n) // 2:
                return False
            if r == m - 1 and c == n - 1:
                return bal == 0

            res = False
            if r + 1 < m:
                res |= dfs(r + 1, c, bal)
            if c + 1 < n:
                res |= dfs(r, c + 1, bal)
            return res

        return dfs(0, 0, 0)