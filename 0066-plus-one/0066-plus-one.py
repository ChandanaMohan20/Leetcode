class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        x=""
        for i in digits:
            val = str(i)
            x+=val
        num = int(x)
        num = num+1
        
        op = []
        numb = str(num)
        for i in numb:
            val = int(i)
            op.append(val)
            
        return op