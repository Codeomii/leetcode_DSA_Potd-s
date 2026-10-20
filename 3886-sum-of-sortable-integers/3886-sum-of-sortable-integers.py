class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        
        pref_max = [0] * (n + 1)
        for i in range(n):
            pref_max[i + 1] = max(pref_max[i], nums[i])
            
        suff_min = [float('inf')] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])
            
        pref_drop = [0] * n
        for i in range(1, n):
            pref_drop[i] = pref_drop[i - 1] + (1 if nums[i - 1] > nums[i] else 0)
            
        divisors = []
        for d in range(1, int(n**0.5) + 1):
            if n % d == 0:
                divisors.append(d)
                if d * d != n:
                    divisors.append(n // d)
                    
        ans = 0
        for k in divisors:
            valid = True
            for start in range(0, n, k):
                end = start + k
                
                if pref_max[start] > suff_min[start]:
                    valid = False
                    break
                    
                drops = pref_drop[end - 1] - pref_drop[start]
                if nums[end - 1] > nums[start]:
                    drops += 1
                    
                if drops > 1:
                    valid = False
                    break
                    
            if valid:
                ans += k
                
        return ans