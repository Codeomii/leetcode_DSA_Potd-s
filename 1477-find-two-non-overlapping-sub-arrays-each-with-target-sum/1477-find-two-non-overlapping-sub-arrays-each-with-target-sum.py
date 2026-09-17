class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n, left, curr, ans, min_len = len(arr), 0, 0, float("inf"), [float("inf")] * len(arr)
        best = float("inf")
        for right in range(n):
            curr += arr[right]
            while curr > target:
                curr -= arr[left]
                left += 1
            if curr == target:
                L = right - left + 1
                if left > 0 and min_len[left - 1] != float("inf"):
                    ans = min(ans, min_len[left - 1] + L)
                best = min(best, L)
            min_len[right] = min(min_len[right - 1] if right > 0 else float("inf"), best)
        return ans if ans != float("inf") else -1