class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n = len(word1)
        m = len(word2)
        
        ans = ""
        for i in range(0,min(m,n)):
            res1 = word1[i] + word2[i]
            ans = ans+ res1
            
        if m>n:
            diff = m-n
            res2 = word2[n:m]
            
            res = ans+res2
            return res
            
        else:
            diff = n-m
            res2 = word1[m:n]
            res = ans+res2
            return res