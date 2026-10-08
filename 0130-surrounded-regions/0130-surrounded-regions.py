from collections import deque

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    if self.bfs((i, j), board):
                        for r, c in self.region:
                            board[r][c] = "X"

    def bfs(self, node, board):
        m = len(board)
        n = len(board[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        qu = deque([node])
        visited = {node}
        self.region = [node]

        touches_boundary = False

        while qu:
            x, y = qu.popleft()

            if x == 0 or x == m-1 or y == 0 or y == n-1:
                touches_boundary = True

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                if (0 <= new_x < m and
                    0 <= new_y < n and
                    board[new_x][new_y] == "O" and
                    (new_x, new_y) not in visited):

                    visited.add((new_x, new_y))
                    self.region.append((new_x, new_y))
                    qu.append((new_x, new_y))

        return not touches_boundary