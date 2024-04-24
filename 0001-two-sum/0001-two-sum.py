class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a= [0 for x in range(0,2)]
        
        for i in range(0, len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+ nums[j] == target):
                    a[0] = i
                    a[1] = j
                    
        return a
                    
                
                