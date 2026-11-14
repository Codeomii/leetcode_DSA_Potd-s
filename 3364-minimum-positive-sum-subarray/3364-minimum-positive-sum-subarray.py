class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')
        for i in range(len(nums)):
            s = 0
            for j in range(i, min(len(nums), i + r)):
                s += nums[j]
                if l <= j - i + 1 <= r and s > 0:
                    ans = min(ans, s)
        return ans if ans != float('inf') else -1