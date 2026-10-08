from collections import deque
class Solution:

    def numEnclaves(self, grid: list[list[int]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        count = 0 

        for i in range (m) :
            for j in range (n):
                if (grid[i][j]==1) and (i,j) not in visited:
                    is_walk_path, cells = self.bfs((i,j),grid,visited)
                    if not is_walk_path:
                        count+=cells
        return count

    def bfs(self,node, grid,visited):
        m = len(grid)
        n = len(grid[0])
        cells=1
        visited.add(node)
        qu = deque([node])
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        no_walk_path = False
        while qu:
            x,y = qu.popleft()
            if (x == 0 or x==m-1 or y==0 or y==n-1):
                no_walk_path = True
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if (0 <= nx < m and
                    0 <= ny < n and
                    grid[nx][ny] == 1 and
                    (nx, ny) not in visited):

                    visited.add((nx, ny))
                    cells+=1
                    qu.append((nx, ny))

        return  no_walk_path, cells
            

