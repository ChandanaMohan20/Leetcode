class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        maxsum = float('-inf')
        
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                numsum = nums[i]+nums[j]
                if numsum>maxsum and numsum<k:
                    maxsum = numsum
        if maxsum<0:
            return -1
        return maxsum
                
                
    
                    
                