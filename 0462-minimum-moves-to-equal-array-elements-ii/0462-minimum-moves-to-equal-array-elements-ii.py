class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = len(nums) // 2
        return sum(abs(x - nums[mid]) for x in nums)