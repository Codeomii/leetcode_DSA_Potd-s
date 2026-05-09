'''3629. Minimum Jumps to Reach End via Prime Teleportation:--

You are given an integer array nums of length n.

You start at index 0, and your goal is to reach index n - 1.

From any index i, you may perform one of the following operations:

Adjacent Step: Jump to index i + 1 or i - 1, if the index is within bounds.
Prime Teleportation: If nums[i] is a prime number p, you may instantly jump to any index j != i such that nums[j] % p == 0.
Return the minimum number of jumps required to reach index n - 1.


Example 1:
Input: nums = [1,2,4,6]
Output: 2
Explanation:
One optimal sequence of jumps is:
Start at index i = 0. Take an adjacent step to index 1.
At index i = 1, nums[1] = 2 is a prime number. Therefore, we teleport to index i = 3 as nums[3] = 6 is divisible by 2.
Thus, the answer is 2.

Example 2:
Input: nums = [2,3,4,7,9]
Output: 2
Explanation:
One optimal sequence of jumps is:
Start at index i = 0. Take an adjacent step to index i = 1.
At index i = 1, nums[1] = 3 is a prime number. Therefore, we teleport to index i = 4 since nums[4] = 9 is divisible by 3.
Thus, the answer is 2.

Example 3:
Input: nums = [4,6,5,8]
Output: 3
Explanation:
Since no teleportation is possible, we move through 0 → 1 → 2 → 3. Thus, the answer is 3.


Constraints:

1 <= n == nums.length <= 105
1 <= nums[i] <= 106'''

# Solution:--

from collections import defaultdict, deque
from math import isqrt

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, isqrt(x) + 1):
                if x % i == 0:
                    return False
            return True
        
        maxv = max(nums)
        spf = list(range(maxv + 1))
        
        for i in range(2, isqrt(maxv) + 1):
            if spf[i] == i:
                for j in range(i * i, maxv + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        
        factors_map = defaultdict(list)
        
        for i, x in enumerate(nums):
            val = x
            seen = set()
            
            while val > 1:
                p = spf[val]
                if p not in seen:
                    factors_map[p].append(i)
                    seen.add(p)
                while val % p == 0:
                    val //= p
        
        q = deque([0])
        dist = [-1] * n
        dist[0] = 0
        used_prime = set()
        
        while q:
            i = q.popleft()
            
            if i == n - 1:
                return dist[i]
            
            if i - 1 >= 0 and dist[i - 1] == -1:
                dist[i - 1] = dist[i] + 1
                q.append(i - 1)
            
            if i + 1 < n and dist[i + 1] == -1:
                dist[i + 1] = dist[i] + 1
                q.append(i + 1)
            
            val = nums[i]
            
            if is_prime(val) and val not in used_prime:
                used_prime.add(val)
                
                for nxt in factors_map[val]:
                    if dist[nxt] == -1:
                        dist[nxt] = dist[i] + 1
                        q.append(nxt)
        
        return -1