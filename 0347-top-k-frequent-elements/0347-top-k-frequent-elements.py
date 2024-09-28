class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count= {}
        
        for i in range(0, len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
                
            else:
                count[nums[i]] = count[nums[i]]+1
        
                
        result = sorted(count, key= lambda x:count[x], reverse=True)
           
        return result[:k]
            