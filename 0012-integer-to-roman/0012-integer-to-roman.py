class Solution:
    def intToRoman(self, num: int) -> str:
        
        d = {"I" : 1, 
              "IV": 4, 
              "V": 5, 
              "IX":9, 
              "X": 10, 
              "XL": 40, 
              "L": 50, 
              "XC": 90, 
              "C": 100, 
              "CD": 400, 
              "D": 500, 
              "CM": 900, 
              "M": 1000}
            
            
        ans = ""
            
        
        for k,v in reversed(d.items()):
            while num>0:
                if v<=num:
                    ans = ans+k
                    num = num-v

                else: 
                    break

        return ans




