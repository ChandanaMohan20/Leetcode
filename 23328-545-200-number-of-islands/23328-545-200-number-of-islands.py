class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def DFS(i,j):
            if i<0 or i>=len(grid) or j <0 or j>=len(grid[0]) or grid[i][j]=="0":
                return 
            
            grid[i][j] = "0"
            DFS(i,j+1)
            DFS(i,j-1)
            DFS(i+1,j)
            DFS(i-1,j)
            
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    count+=1
                    DFS(i,j)
                    
        return count



            