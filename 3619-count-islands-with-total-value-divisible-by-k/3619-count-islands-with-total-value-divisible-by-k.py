from collections import deque
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        count = 0
        for i in range (m):
            for j in range (n):
                if (i,j) not in visited and grid[i][j]!=0:
                    if self.bfs((i,j),grid, visited)%k==0:
                        count +=1
        return count
        
    def bfs(self,node, grid, visited):
        m = len(grid)
        n = len(grid[0])
        sum = 0
        qu = deque([node])
        visited.add(node)
        dir = [(1,0),(-1,0),(0,1),(0,-1)]

        while qu:
            i,j = qu.popleft()
            sum+=grid[i][j]
            for di,dj in dir:
                ni = i+di
                nj = j+dj
                if (0<=ni<m and 0<=nj<n) and grid[ni][nj]!=0 and (ni,nj) not in visited :
                    visited.add((ni,nj))
                    qu.append((ni,nj))   
        return sum


