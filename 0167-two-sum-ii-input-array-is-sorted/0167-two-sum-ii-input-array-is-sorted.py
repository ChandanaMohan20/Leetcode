class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res= []
        
        l = 0
        r = len(numbers)-1
        
        while(l<r):
            numsum = numbers[l]+numbers[r]
            if numsum==target:
                return[l+1,r+1]
            elif numsum>target:
                r = r-1
            else:
                l=l+1
              
            
            