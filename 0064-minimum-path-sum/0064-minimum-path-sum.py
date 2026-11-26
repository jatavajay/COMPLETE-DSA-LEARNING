class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[0] * m for _ in range(n)]

        dp[0][0] = grid[0][0]

        # First row
        for j in range(1, m):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        # First column
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        # Remaining cells
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = grid[i][j] + min(
                    dp[i-1][j],
                    dp[i][j-1]
                )

        return dp[n-1][m-1]