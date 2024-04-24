class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            a = [[1]]
            return a[0]
        
        elif rowIndex==1:
            a=[[1]]
            a.append([1,1])
            return a[1]
        
        a=[[1]]
        a.append([1,1])
        
        for i in range(2,rowIndex+1):
            temp = [1]
            for j in range(1,i):
                temp.append(a[i-1][j-1]+a[i-1][j])
            temp.append(1)
            
            a.append(temp)
        
        return a[rowIndex]