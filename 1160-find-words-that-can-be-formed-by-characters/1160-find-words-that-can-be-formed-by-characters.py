from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        hm1 ={}
        
        for i in chars:
            if i not in hm1:
                hm1[i] = 1
            else:
                hm1[i]+=1     
        
        valid = 0
        for strs in words:
            wordcount = Counter(strs)
            length = 0
            canform = True
            
            for i in wordcount:
                if wordcount[i]>hm1.get(i,0):
                    canform = False
                    break
            if canform:
                length =len(strs)
                valid +=length
        return valid

                    
            
            