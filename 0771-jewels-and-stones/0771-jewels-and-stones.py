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
            if i in j:
                count = count+1
        
        
            
        return count