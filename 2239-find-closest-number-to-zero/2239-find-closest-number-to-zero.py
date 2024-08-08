class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[]
       
        
        for i in range (0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]> nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
            
        val = 100000000
        for i in nums:
            
            res = abs(i-0)
            
            if res<= val :
                val = res
                num = i
                
        return num

            
            
            