class Solution:
    def countCommas(self, n: int) -> int:
        return sum(max(0, n - 10**k + 1) for k in range(3, 16, 3))