class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        Slen = len(s)
        Tlen = len(t)
        
        if Slen > Tlen :
            return False
        if s == "":
            return True
        
        j = 0
        
        for i in range(0,Tlen):
            if t[i] == s[j]:
                if j == Slen - 1:
                    return True
                j = j+1
                
        return False
    
        