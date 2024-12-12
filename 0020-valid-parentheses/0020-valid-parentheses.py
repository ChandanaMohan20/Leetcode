
class Solution:
    
    def isValid(self, s: str) -> bool:
        MAXLEN = 10**4
        slen = len(s)
        
        if slen > 10**4:
            return False
        if len(s)==0:
            return False
        if len(s)==1:
            return False
        
        stack=[]
        hashmap = {')':'(',']':'[', '}':'{'}
        
        for char in s:
            if char in hashmap.values():
                stack.append(char)
            elif char in hashmap.keys():
                if stack and stack[-1]==hashmap[char]:
                    stack.pop()
                    
                else:
                    return False
            else:
                return False
            
        if len(stack)==0:
            return True
        
        else:
            return False
            