class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = 0
        r = len(nums) -1
        a = []
        while l<=r:
            if nums[l]*nums[l] > nums[r]* nums[r]:
                a.append(nums[l]*nums[l])
                l=l+1
                
            else:
                a.append(nums[r]*nums[r])
                r = r-1
                
        return a[::-1]