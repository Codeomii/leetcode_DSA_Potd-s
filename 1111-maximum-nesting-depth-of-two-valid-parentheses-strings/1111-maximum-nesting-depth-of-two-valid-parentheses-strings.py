class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        d = 0
        ans = []
        for c in seq:
            if c == '(':
                d += 1
                ans.append(d & 1)
            else:
                ans.append(d & 1)
                d -= 1
        return ans