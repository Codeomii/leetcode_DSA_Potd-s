class Solution:
    def resultArray(self, nums, k):
        dp = [0] * k
        ans = [0] * k
        for n in nums:
            ndp = [0] * k
            ndp[n % k] += 1
            for r in range(k):
                ndp[r * (n % k) % k] += dp[r]
            dp = ndp
            for r in range(k):
                ans[r] += dp[r]
        return ans