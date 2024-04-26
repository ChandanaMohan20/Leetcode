class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        
        xstr = str(x)
        xrev = xstr[::-1]
        
        if(xstr==xrev):
            return True
        else:
            return False
      
    