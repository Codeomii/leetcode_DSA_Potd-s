class Solution:

    def maxPalindromes(self, s: str, k: int) -> int:
        ans, last = 0, -1
        for i in range(2 * len(s) - 1):
            l, r = i // 2, i // 2 + i % 2
            while l > last and r < len(s) and s[l] == s[r]:
                if r - l + 1 >= k:
                    ans, last = ans + 1, r
                    break
                l, r = l - 1, r + 1
        return ans