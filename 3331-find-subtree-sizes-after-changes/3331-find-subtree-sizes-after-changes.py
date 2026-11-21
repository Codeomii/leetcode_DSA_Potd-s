class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]

        for i in range(1, n):
            adj[parent[i]].append(i)

        new_parent = parent[:]
        last = {}
        stack = [(0, -1, 0)]

        while stack:
            u, prev, state = stack.pop()

            if state == 0:
                c = s[u]
                prev = last.get(c, -1)

                if u and prev != -1:
                    new_parent[u] = prev

                last[c] = u
                stack.append((u, prev, 1))

                for v in reversed(adj[u]):
                    stack.append((v, -1, 0))
            else:
                c = s[u]
                if prev == -1:
                    del last[c]
                else:
                    last[c] = prev

        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[new_parent[i]].append(i)

        order = [0]
        for u in order:
            order.extend(tree[u])

        ans = [1] * n
        for u in reversed(order[1:]):
            ans[new_parent[u]] += ans[u]

        return ans