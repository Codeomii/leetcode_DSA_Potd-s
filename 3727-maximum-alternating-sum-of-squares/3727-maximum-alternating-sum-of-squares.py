from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        a = sorted((x*x for x in nums), reverse=True)
        k = (len(a) + 1) // 2
        return sum(a[:k]) - sum(a[k:])