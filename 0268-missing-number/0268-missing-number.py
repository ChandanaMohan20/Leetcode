class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxval = nums[0]
        
        for i in range(0,len(nums)):
            if maxval> nums[i]:
                maxval = nums[i]
                
        nums.sort()
                        
                
                        
        for i in range(0,len(nums)):
            if nums[i]!=i:
                return i
        return len(nums)
            
            
            