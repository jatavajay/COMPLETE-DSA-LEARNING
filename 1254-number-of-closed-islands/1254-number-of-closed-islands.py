from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]
        count = 0

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0 and not visited[i][j]:
                    if self.dfs(i, j, grid, visited, m, n):
                        count += 1
        return count

    def dfs(self, i, j, grid, visited, m, n):
        visited[i][j] = True
        if i == 0 or j == 0 or i == m-1 or j == n-1:
            return False
        closed = True
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for di, dj in directions:
            ni = i + di
            nj = j + dj

            if grid[ni][nj] == 0 and not visited[ni][nj]:
                if not self.dfs(ni, nj, grid, visited, m, n):
                    closed = False

        return closed
