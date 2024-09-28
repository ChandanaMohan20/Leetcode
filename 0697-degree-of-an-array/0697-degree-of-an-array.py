class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        start = {}
        end = {}
        
        for i in range(0, len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
                end[nums[i]] = i
                start[nums[i]] = i
                
            else:
                count[nums[i]] = count[nums[i]] + 1
                end[nums[i]] = i
                
        maxfreq = max(count.values())
        
        result = []
        
        for i,j in count.items():
            if j == maxfreq :
                total = end[i] - start[i] + 1
                result.append(total)
        return min(result)