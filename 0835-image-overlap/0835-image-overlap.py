from collections import Counter

class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        pts1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c]]
        pts2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c]]
        
        counts = Counter((r1 - r2, c1 - c2) for r1, c1 in pts1 for r2, c2 in pts2)
        return max(counts.values(), default=0)