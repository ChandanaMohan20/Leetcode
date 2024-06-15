class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l =1
        n = len(nums)
        
        for r in range(1,n):
            if nums[r]!=nums[r-1]:
                nums[l] = nums[r]
                l = l+1
                
        return l