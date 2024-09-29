class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count={}
        last = {}
        
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = 1
                last[s[i]] = i
            else:
                count[s[i]] +=1
                
        minfre = min(count.values())
        
        if minfre!=1:
            return -1
        
        res = []
       

        for i,j in count.items():
            if j == minfre:
                res.append(i)
        
       
        for i,j in last.items():
            if i==res[0]:
                return j 

       