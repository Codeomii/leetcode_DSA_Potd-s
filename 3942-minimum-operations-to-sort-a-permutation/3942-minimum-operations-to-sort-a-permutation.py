class Solution:

  def minOperations(self, nums: List[int]) -> int:
    n, z = len(nums), nums.index(0)
    chk = lambda s: all(
        nums[(z + (i - 1) * s) % n] <= nums[(z + i * s) % n] for i in range(1, n)
    )

    res = []
    if chk(1):
      res.extend([z, n - z + 2])
    if chk(-1):
      res.extend([z + 2, n - z])

    return min(res) if res else -1