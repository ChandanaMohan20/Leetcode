class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        count = {}
        
        for s in strs:
            for i in range(1, len(s)+1):
                
                prefix = s[:i]
                
                if prefix not in count:
                    count[prefix] = 1
                else:
                    count[prefix] +=1
                    
        long = ""
        
        for i, j in count.items():
            if j == len(strs) and len(i)> len(long):
                long = i
                
        return long