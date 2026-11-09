import heapq

class Solution:
    def busiestServers(self, k, arrival, load):
        bit = [0] * (k + 1)

        for i in range(1, k + 1):
            bit[i] = i & -i

        def update(i, val):
            i += 1
            while i <= k:
                bit[i] += val
                i += i & -i

        def query(i):
            s = 0
            while i:
                s += bit[i]
                i -= i & -i
            return s

        def find(x):
            idx = 0
            p = 1 << (k.bit_length() - 1)
            while p:
                nxt = idx + p
                if nxt <= k and bit[nxt] < x:
                    idx = nxt
                    x -= bit[nxt]
                p >>= 1
            return idx

        busy = []
        count = [0] * k

        for i, (t, l) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= t:
                _, server = heapq.heappop(busy)
                update(server, 1)

            total = query(k)
            if total == 0:
                continue

            start = i % k
            before = query(start)

            if total > before:
                server = find(before + 1)
            else:
                server = find(1)

            update(server, -1)
            count[server] += 1
            heapq.heappush(busy, (t + l, server))

        mx = max(count)
        return [i for i in range(k) if count[i] == mx]