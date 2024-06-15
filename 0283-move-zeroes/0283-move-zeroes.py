class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=0
        val = 0
        n = len(nums)
        count = 0
        for i in nums:
            if i==val:
                count = count+1

        for i in range(0,n):
            if nums[i]!= val:
                nums[l]= nums[i]
                l = l+1

        
        for i in range(0, count):
            nums[n-i-1] = 0
        

