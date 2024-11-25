class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        HMttos={}
        HMstot={}
        
        if len(s)!=len(t):
            return False
        
        for chars, chart in zip(s,t):
            if chars in HMstot:
                if HMstot[chars]!=chart:
                    return False
            else:
                HMstot[chars]=chart
            if chart in HMttos:
                if HMttos[chart]!=chars:
                    return False
            else:
                HMttos[chart]=chars
                
        return True