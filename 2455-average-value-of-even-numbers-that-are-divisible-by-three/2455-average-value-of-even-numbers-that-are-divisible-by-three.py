class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        value = []
        
        numlen =len(nums)
        for i in nums:
            if i%6==0:
                value.append(i)
                
            
        vallen = len(value)
        if vallen==0:
            return 0
        avg = sum(value)/vallen
        
        return avg
                