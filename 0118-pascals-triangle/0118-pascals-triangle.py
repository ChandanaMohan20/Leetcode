class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows ==1:
            a = [[1]]
            return a
        if numRows==2:
            
            a = [[1]]
            a.append([1,1])
            return a 
        
        a = [[1]]
        a.append([1,1])
        
        for i in range (2,numRows):
            temp=[1]
            for j in range(1,i):
               
                temp.append(a[i-1][j-1] + a[i-1][j])
            temp.append(1)
            a.append(temp)
                
        return a
                
                
        