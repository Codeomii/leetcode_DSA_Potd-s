class Solution:
    def removeInvalidParentheses(self, s):
        def valid(x):
            c = 0
            for ch in x:
                c += (ch == '(') - (ch == ')')
                if c < 0: return False
            return c == 0

        q, seen = {s}, {s}
        while q:
            ans = [x for x in q if valid(x)]
            if ans: return ans
            nq = set()
            for x in q:
                for i in range(len(x)):
                    if x[i] in '()':
                        y = x[:i] + x[i+1:]
                        if y not in seen:
                            seen.add(y); nq.add(y)
            q = nq