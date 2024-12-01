class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        revs = s[::-1]
        for i in range(len(s)-1):
            
            subs =  s[i:i+2]
            
            if subs in revs :
                return True
            subs=""
        return False