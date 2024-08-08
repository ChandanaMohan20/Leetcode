class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        j = list(jewels)
        s = list(stones)
        
        count = 0
        
        for i in s:
            for k in j:
                if i == k:
                    count = count+1
        
        
            
        return count