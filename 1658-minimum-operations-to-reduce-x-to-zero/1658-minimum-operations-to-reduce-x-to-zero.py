class Solution:
    def minOperations(self, nums, x):
        target = sum(nums) - x
        if target < 0: return -1
        cur = l = best = 0
        for r,v in enumerate(nums):
            cur += v
            while cur > target:
                cur -= nums[l]
                l += 1
            if cur == target: best = max(best,r-l+1)
        return len(nums)-best if best else (-1 if target else len(nums))