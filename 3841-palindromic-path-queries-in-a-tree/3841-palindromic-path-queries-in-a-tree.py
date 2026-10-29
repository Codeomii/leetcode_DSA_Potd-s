class Solution:
    def palindromePath(self, n, edges, s, queries):
        from collections import deque

        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        LOG = n.bit_length()
        tin = [0] * n
        tout = [0] * n
        dep = [0] * n
        par = [[0] * n for _ in range(LOG)]
        order = []
        stack = [(0, 0, 0)]

        while stack:
            u, p, state = stack.pop()
            if state == 0:
                tin[u] = len(order)
                order.append(u)
                par[0][u] = p
                stack.append((u, p, 1))
                for v in reversed(g[u]):
                    if v != p:
                        dep[v] = dep[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = len(order)

        for j in range(1, LOG):
            for u in range(n):
                par[j][u] = par[j - 1][par[j - 1][u]]

        def lca(u, v):
            if dep[u] < dep[v]:
                u, v = v, u
            d = dep[u] - dep[v]
            for j in range(LOG):
                if d >> j & 1:
                    u = par[j][u]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if par[j][u] != par[j][v]:
                    u, v = par[j][u], par[j][v]
            return par[0][u]

        bit = [0] * (n + 1)

        def add(i, x):
            i += 1
            while i <= n:
                bit[i] ^= x
                i += i & -i

        def pref(i):
            x = 0
            while i:
                x ^= bit[i]
                i -= i & -i
            return x

        s = list(s)
        for u in range(n):
            x = 1 << (ord(s[u]) - 97)
            add(tin[u], x)
            add(tout[u], x)

        def rootmask(u):
            return pref(tin[u] + 1)

        ans = []
        for q in queries:
            a = q.split()
            if a[0] == "update":
                u, c = int(a[1]), a[2]
                x = (1 << (ord(s[u]) - 97)) ^ (1 << (ord(c) - 97))
                add(tin[u], x)
                add(tout[u], x)
                s[u] = c
            else:
                u, v = int(a[1]), int(a[2])
                w = lca(u, v)
                mask = rootmask(u) ^ rootmask(v) ^ (1 << (ord(s[w]) - 97))
                ans.append(mask.bit_count() <= 1)

        return ans