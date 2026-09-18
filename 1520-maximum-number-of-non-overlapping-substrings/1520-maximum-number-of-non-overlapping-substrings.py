class Solution:

    def maxNumOfSubstrings(self, s: str) -> list[str]:
        L, R = {c: s.find(c) for c in set(s)}, {c: s.rfind(c) for c in set(s)}
        valid = []
        for c, l in L.items():
            r, i = R[c], l
            while i <= r and L[s[i]] >= l:
                r, i = max(r, R[s[i]]), i + 1
            if i > r:
                valid.append((l, r))

        res, prev = [], -1
        for l, r in sorted(valid, key=lambda x: x[1]):
            if l > prev:
                res.append(s[l : r + 1])
                prev = r
        return res