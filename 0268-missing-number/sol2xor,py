class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = 0
        
        for i in range(0,len(nums)+1):
            res = res ^ i
            
        for num in nums:
            res = num ^ res
            
        return res
