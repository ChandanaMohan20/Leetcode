class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        
        ans = []
        
        MaxLen = 20
        
        if n>MaxLen:
            n = 20
        Minval = -(2 **31)
        Maxval = (2**31) -1
        
        i=0
        start = 0
        end = n
        
        for i in range(n):
            if nums[i]>=Minval:
                start = i
                break
                
        for i in range(n-1,-1,-1):
            if nums[i] <= Maxval:
                end = i+1
                break
                
        i = 0
        
        nums = nums[start:end]
        
        while i<len(nums):
            start = nums[i]
            
            while i+1< len(nums) and nums[i+1]==nums[i]+1:
                i = i+1
            if start != nums[i]:
                ans.append(str(start)+"->"+str(nums[i]))
            else:
                ans.append(str(nums[i]))
                
            i  = i+1
        return ans
            
                