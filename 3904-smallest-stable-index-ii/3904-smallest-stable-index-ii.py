class Solution:
    def firstStableIndex(self, nums, k):
        mn=[0]*len(nums); mn[-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1): mn[i]=min(mn[i+1],nums[i])
        mx=nums[0]
        for i,x in enumerate(nums):
            mx=max(mx,x)
            if mx-mn[i]<=k:return i
        return -1