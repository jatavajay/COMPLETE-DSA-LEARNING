class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        w = len(grid)
        l = len(grid[0])
        visited= set()
        maxarea = 0
        for i in range (w):
            for j in range (l):
                if grid[i][j]==1:
                    visited.add((i,j))
                    res = self.dfs([i,j],visited,grid)
                    maxarea = max(maxarea,res)
        return maxarea
        
    def dfs(self, node, visited,grid):
        w = len(grid)
        l = len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        area = 1
        for neighbour in directions:
            new_i = neighbour[0]+node[0]
            new_j = neighbour[1]+node[1]
            if (new_i>=0 and new_i<w) and (new_j>=0 and new_j<l) and grid[new_i][new_j]==1 and (new_i,new_j) not in visited :
                
                visited.add((new_i, new_j))
                area+=self.dfs((new_i,new_j),visited,grid)
                
        return area
            
