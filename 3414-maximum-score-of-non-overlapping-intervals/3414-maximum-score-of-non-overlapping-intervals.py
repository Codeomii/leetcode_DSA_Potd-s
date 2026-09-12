from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        A = sorted([(l, r, w, i) for i, (l, r, w) in enumerate(intervals)], key=lambda x: x[1])
        E, dp = [x[1] for x in A], [[(0, [])] * 5 for _ in range(len(A) + 1)]
        for i, (l, r, w, idx) in enumerate(A, 1):
            j = bisect_right(E, l - 1)
            for k in range(1, 5):
                c2 = (dp[j][k - 1][0] + w, sorted(dp[j][k - 1][1] + [idx]))
                c1 = dp[i - 1][k]
                dp[i][k] = c2 if c2[0] > c1[0] or (c2[0] == c1[0] and c2[1] < c1[1]) else c1
        return dp[-1][4][1]