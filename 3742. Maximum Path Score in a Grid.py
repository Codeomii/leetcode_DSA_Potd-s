'''3742. Maximum Path Score in a Grid:--

You are given an m x n grid where each cell contains one of the values 0, 1, or 2. You are also given an integer k.

You start from the top-left corner (0, 0) and want to reach the bottom-right corner (m - 1, n - 1) by moving only right or down.

Each cell contributes a specific score and incurs an associated cost, according to their cell values:

0: adds 0 to your score and costs 0.
1: adds 1 to your score and costs 1.
2: adds 2 to your score and costs 1. ​​​​​​​
Return the maximum score achievable without exceeding a total cost of k, or -1 if no valid path exists.

Note: If you reach the last cell but the total cost exceeds k, the path is invalid.


Example 1:

Input: grid = [[0, 1],[2, 0]], k = 1
Output: 2

Explanation:
The optimal path is:

Cell	grid[i][j]	Score	Total
Score	Cost	Total
Cost
(0, 0)	0	0	0	0	0
(1, 0)	2	2	2	1	1
(1, 1)	0	0	2	0	1
Thus, the maximum possible score is 2.

Example 2:

Input: grid = [[0, 1],[1, 2]], k = 1
Output: -1

Explanation:

There is no path that reaches cell (1, 1)​​​​​​​ without exceeding cost k. Thus, the answer is -1.

Constraints:

1 <= m, n <= 200
0 <= k <= 103​​​​​​​
​​​​​​​grid[0][0] == 0
0 <= grid[i][j] <= 2'''

# Solution :--

class Solution:
    def maxPathScore(self, grid, k):
        m, n = len(grid), len(grid[0])
        cost_map = {0: 0, 1: 1, 2: 1}
        score_map = {0: 0, 1: 1, 2: 2}
        
        dp = [[dict() for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0
        
        for i in range(m):
            for j in range(n):
                for cost, score in list(dp[i][j].items()):
                    if j + 1 < n:
                        nc = cost + cost_map[grid[i][j+1]]
                        ns = score + score_map[grid[i][j+1]]
                        if nc <= k:
                            if nc not in dp[i][j+1] or dp[i][j+1][nc] < ns:
                                dp[i][j+1][nc] = ns
                    if i + 1 < m:
                        nc = cost + cost_map[grid[i+1][j]]
                        ns = score + score_map[grid[i+1][j]]
                        if nc <= k:
                            if nc not in dp[i+1][j] or dp[i+1][j][nc] < ns:
                                dp[i+1][j][nc] = ns
        
        return max(dp[m-1][n-1].values()) if dp[m-1][n-1] else -1
        