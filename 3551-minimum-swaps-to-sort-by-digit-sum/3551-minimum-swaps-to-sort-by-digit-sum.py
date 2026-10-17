class Solution:
    def minSwaps(self, nums):
        a = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))
        pos = {v: i for i, v in enumerate(a)}
        vis = [False] * len(nums)
        ans = 0
        for i in range(len(nums)):
            if vis[i] or pos[nums[i]] == i:
                continue
            j, cnt = i, 0
            while not vis[j]:
                vis[j] = True
                j = pos[nums[j]]
                cnt += 1
            ans += cnt - 1
        return ans