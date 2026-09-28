class Solution:
    def maxDepth(self, s: str) -> int:
        return max(accumulate(s, lambda depth, ch: depth + (ch == '(') - (ch == ')'), initial=0))