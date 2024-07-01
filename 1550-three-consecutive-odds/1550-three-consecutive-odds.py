class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        n = len(arr)
        flag1 = 0
        flag2 = 0
        for i in range(0,n-2):
            if (arr[i]%2 !=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0):
                return True
            
        return False