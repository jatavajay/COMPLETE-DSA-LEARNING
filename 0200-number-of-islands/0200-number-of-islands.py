class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        w = len(grid)
        l = len(grid[0])
        visited = set()
        count = 0
        for i in range (w):
            for j in range (l):
                if grid[i][j]=="1" and (i,j) not in visited:
                    visited.add((i,j))
                    count+=1
                    self.bfs((i,j),grid,visited)
        return count
    def bfs(self,node,grid,visited):
        w = len(grid)
        l = len(grid[0])
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        x,y = node
        for neighbour in direction:
            new_x = x+neighbour[0]
            new_y = y+neighbour[1]
            if (new_x>=0 and new_x<w and new_y >=0 and new_y<l and grid[new_x][new_y]=="1" and (new_x, new_y) not in visited):
                visited.add((new_x,new_y))
                self.bfs((new_x,new_y),grid,visited)
        