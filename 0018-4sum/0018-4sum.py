class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(0,n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l = j+1
                r = n-1
                
                while(l<r):
                    numsum = nums[i]+nums[j]+nums[l]+nums[r]
                    if numsum < target:
                        l = l+1
                    elif numsum > target:
                        r = r-1
                    else:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        
                        while l<r and nums[l]==nums[l+1]:
                            l = l+1
                        while l<r and nums[r]==nums[r-1]:
                            r = r-1
                        l = l+1
                        r = r-1
                    
        return res
                        
                
            