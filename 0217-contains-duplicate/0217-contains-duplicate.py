class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = list(set(nums))
        
        if len(temp)==len(nums):
            return False
        else:
            return True