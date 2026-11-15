class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = even = ans = 0
        s = 0
        for x in arr:
            s += x
            if s % 2:
                ans += even + 1
                odd += 1
            else:
                ans += odd
                even += 1
        return ans % (10**9 + 7)