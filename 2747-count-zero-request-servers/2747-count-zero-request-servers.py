class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])
        q = sorted((t, i) for i, t in enumerate(queries))
        ans = [0] * len(queries)
        cnt = {}
        l = r = 0

        for t, i in q:
            while r < len(logs) and logs[r][1] <= t:
                s = logs[r][0]
                cnt[s] = cnt.get(s, 0) + 1
                r += 1

            while l < r and logs[l][1] < t - x:
                s = logs[l][0]
                cnt[s] -= 1
                if cnt[s] == 0:
                    del cnt[s]
                l += 1

            ans[i] = n - len(cnt)

        return ans