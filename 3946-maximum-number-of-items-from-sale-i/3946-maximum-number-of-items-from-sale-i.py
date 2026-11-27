class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        bonus = [sum(i != j and y % x == 0 for j, (y, _) in enumerate(items)) for i, (x, _) in enumerate(items)]

        dp = [0] * (budget + 1)

        for (_, p), b in zip(items, bonus):
            ndp = dp[:]

            for j in range(p, budget + 1):
                ndp[j] = max(ndp[j], dp[j-p] + b + 1)

            for j in range(budget + 1):
                if ndp[j] >= 0 and j + p <= budget:
                    ndp[j+p] = max(ndp[j+p], ndp[j] + 1)

            dp = ndp

        return max(dp)