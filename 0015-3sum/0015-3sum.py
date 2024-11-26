class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res= []
        nums.sort()
        n = len(nums)
        for i in range(0, n-2):
            if i>0 and nums[i]==nums[i-1]:# skipping dupe
                continue
            l = i+1
            r = n-1
            while(l<r):
                numsum = nums[i]+nums[l]+nums[r]
                if numsum>0:
                    r = r-1
                elif numsum<0:
                    l = l+1
                else:
                    a = [nums[i],nums[l],nums[r]]
                    
                    res.append(a)
                    while l<r and nums[l]==nums[l+1]: #skipping dupe
                        l = l+1
                    while l<r and nums[r]==nums[r-1]: #skipping dupe
                        r = r-1
                    
                    l = l+1
                    r = r-1
                    
        return res