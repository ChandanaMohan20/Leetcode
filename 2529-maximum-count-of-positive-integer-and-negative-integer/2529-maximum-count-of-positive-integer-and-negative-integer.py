class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg = 0
        pos = 0
        for i in range(0,len(nums)):
            if nums[i]<0:
                neg = neg+1
                
            if nums[i]>0:
                pos = pos+1
                
        if neg>pos:
            return neg
        else:
            return pos