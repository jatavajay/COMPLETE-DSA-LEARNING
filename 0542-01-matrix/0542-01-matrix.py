from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        l = len(mat)
        w = len(mat[0])
        output = [[0 for _ in range(w)] for _ in range(l)]
        qu = deque()

        for i in range(l):
            for j in range(w):
                if mat[i][j] == 0:
                    qu.append((i, j))
                else:
                    output[i][j] = -1  
        return self.bfs(qu, output)
    def bfs(self, qu, output):
        l = len(output)
        w = len(output[0])
        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        while qu:
            x, y = qu.popleft()
            for dx, dy in direction:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < l and 0 <= new_y < w:
                    # If not visited
                    if output[new_x][new_y] == -1:
                        output[new_x][new_y] = output[x][y] + 1
                        qu.append((new_x, new_y))
        return output