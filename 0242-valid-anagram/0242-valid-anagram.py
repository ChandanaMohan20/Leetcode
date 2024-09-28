class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        check1 = ''. join(sorted(s))
        check2 = ''. join(sorted(t))
        
        if check1 == check2 :
            return True
        else:
            return False