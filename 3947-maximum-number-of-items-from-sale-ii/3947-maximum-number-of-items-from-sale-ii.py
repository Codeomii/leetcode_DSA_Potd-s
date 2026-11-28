
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        mx = max(x[0] for x in items)

        freq = [0] * (mx + 1)
        for f, p in items:
            freq[f] += 1

        gain = [0] * (mx + 1)
        for i in range(1, mx + 1):
            for j in range(i, mx + 1, i):
                gain[i] += freq[j]
            if freq[i]:
                gain[i] -= 1

        items.sort(key=lambda x: x[1])
        mn = items[0][1]
        ans = 0

        for f, p in items:
            if p >= 2 * mn:
                break

            take = min(gain[f], budget // p)
            ans += 2 * take
            budget -= take * p

        return ans + budget // mn
