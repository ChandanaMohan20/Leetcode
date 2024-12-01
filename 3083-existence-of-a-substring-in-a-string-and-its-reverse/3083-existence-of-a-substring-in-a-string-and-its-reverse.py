class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(len(s)-1):
            
            subs =  s[i:i+2]
            revs = s[::-1]
            if subs in revs :
                return True
            subs=""
        return False