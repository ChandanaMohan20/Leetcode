class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numlen = len(nums)
        
        for i in nums:
            if nums.count(i)>numlen//2:
                return i