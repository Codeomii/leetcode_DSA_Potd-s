class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD, added = 10**9 + 7, {}
        for char in s:
            added[char] = (sum(added.values()) + 1) % MOD
        return sum(added.values()) % MOD