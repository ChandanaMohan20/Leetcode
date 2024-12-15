class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm1 = {}
        hm2 = {}
        
        for i in ransomNote:
            if i not in hm1:
                hm1[i] = 1
            else:
                hm1[i]+=1
        
        for i in magazine:
            if i not in hm2:
                hm2[i] = 1
            else:
                hm2[i]+=1
                
        for i,j in hm1.items():
            if i not in hm2.keys():
            
                return False
            if j> hm2[i]:
                return False
        return True
            
                
        
                
                
                