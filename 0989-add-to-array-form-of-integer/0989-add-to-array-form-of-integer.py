class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        numstr=""
        
        for i in num:
            val = str(i)
            numstr+=val
            
        
        op = []
        numval = int(numstr)
        numval = numval+k
        numstr = str(numval)
        for i in numstr:
            val = int(i)
            op.append(val)
            
        return op