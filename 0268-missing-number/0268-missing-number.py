class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = 0
        numsum = 0
        for i in range(len(nums)):
            res = res + i
            numsum = numsum + nums[i]
            
        ans = res+len(nums)-numsum
        return ans