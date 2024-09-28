class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort(key = lambda x: x[0])
        
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            last = res[-1]
            current = intervals[i]
            
            if current[0]<=last[1]:
                last[1] = max(last[1],current[1])
            else:
                res.append(current)
                
        return res