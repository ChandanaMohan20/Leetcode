class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s= s.lower()
        newstr = ""
        
        for c in s:
            if c.isalnum():
                newstr = newstr + c
        revstr = newstr[::-1]
        
        if newstr==revstr:
            return True
        return False
        
       