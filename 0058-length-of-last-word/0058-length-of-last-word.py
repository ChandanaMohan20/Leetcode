class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = list(s.split(" "))
        
        xlen = len(x)
        y =[]
        
        for i in x:
            if len(i)!=0:
                y.append(i)
        ylen = len(y)
        val = y[ylen-1]
        
        return len(val)