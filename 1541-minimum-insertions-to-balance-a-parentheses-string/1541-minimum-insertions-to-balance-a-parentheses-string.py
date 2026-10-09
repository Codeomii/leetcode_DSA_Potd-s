class Solution:
    def minInsertions(self, s: str) -> int:
        ans = bal = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                bal += 2
                if bal % 2:
                    ans += 1
                    bal -= 1
            else:
                bal -= 1
                if bal < 0:
                    ans += 1
                    bal = 1
            i += 1
        return ans + bal