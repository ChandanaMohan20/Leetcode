class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        
        numlen = len(nums)
        nums.sort()
        if numlen ==1:
            return nums[0]
        
        elif numlen==0:
            return nums[1]
        
        else:
            return nums[numlen-3]