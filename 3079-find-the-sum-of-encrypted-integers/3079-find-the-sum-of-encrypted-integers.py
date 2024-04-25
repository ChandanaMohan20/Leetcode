class Solution(object):
    def sumOfEncryptedInt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numlen = len(nums)
        a = []
        b = []
        
        for i in range(0,numlen):
            ipstr = str(nums[i])
            
            
            for char in ipstr:
                a.append(int(char))
            val = max(a)
            a = []

            iplen = len(ipstr)
            evalue = str(val)*iplen
            b.append(int(evalue))
        return(sum(b))
                
            
            