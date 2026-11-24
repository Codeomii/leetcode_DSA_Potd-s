
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        from math import gcd

        ans = 0
        n = len(nums)

        for i in range(n):
            p, g, l = 1, 0, 1

            for j in range(i, n):
                x = nums[j]
                p *= x
                g = gcd(g, x)
                l = l * x // gcd(l, x)

                if p == g * l:
                    ans = max(ans, j - i + 1)

        return ans
