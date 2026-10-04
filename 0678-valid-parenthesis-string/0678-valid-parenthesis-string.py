class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            lo = max(lo, 0)
            if hi < 0: return False
        return lo == 0