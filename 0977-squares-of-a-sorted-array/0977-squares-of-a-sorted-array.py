class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = []
        for i in range(0,len(nums)):
            val = nums[i] * nums[i]
            a.append(val)
            
        a.sort()
                
                
        return a
            