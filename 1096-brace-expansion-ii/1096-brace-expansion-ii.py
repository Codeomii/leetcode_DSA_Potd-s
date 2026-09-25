class Solution:
    def braceExpansionII(self, expression):
        def parse():
            res = {""}
            while i[0] < len(expression) and expression[i[0]] != '}':
                if expression[i[0]] == ',':
                    i[0] += 1
                    res |= parse()
                else:
                    if expression[i[0]] == '{':
                        i[0] += 1
                        cur = parse()
                        i[0] += 1
                    else:
                        cur = {expression[i[0]]}
                        i[0] += 1
                    res = {a + b for a in res for b in cur}
            return res

        i = [0]
        return sorted(parse())