class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()

        x,y = 0,0

        visited.add((x,y))

        for i in path:
            if i=='N':
                y+=1
            if i=='S':
                y-=1
            if i=='E':
                x+=1
            if i=='W':
                x-=1
            if (x,y) in visited:
                return True
            visited.add((x,y))

        return False