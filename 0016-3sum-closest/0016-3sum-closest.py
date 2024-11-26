class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        HM = {}
        nums.sort()
        closesum = float('-inf')
        for i in range(0,n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i+1
            r = n-1
            
            while(l<r):
                numsum = nums[i]+ nums[l]+ nums[r]
                if abs(numsum-target)<abs(closesum-target):
                    closesum = numsum
                if numsum<target:
                    l = l+1
                elif numsum>target:
                    r = r-1
                else:
                    return target
        return closesum
            
                
                
            