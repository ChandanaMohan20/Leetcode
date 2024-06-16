class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX = 2**31
        MIN = -2**31
        
        if (x >= MAX or x < MIN):
            ans = 0
            return ans
        
        
         
        rev_num = 0
        num = abs(x)

        while num:


            rev_num = rev_num *10

            rev_num = rev_num + num %10

            num = num/10

        if x<0 :
            ans = -rev_num
            
        else:
            ans = rev_num
            
        if ans<MIN or ans >=MAX:
            return 0
        else:
            return ans
        










