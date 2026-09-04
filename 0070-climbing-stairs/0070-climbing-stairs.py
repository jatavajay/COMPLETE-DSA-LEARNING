class Solution:
    # Top down + Memoization Approach
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        return self.calculateSteps(dp,n)
    def calculateSteps(self, dp, n):
        if n<=2:
            return n
        if dp[n]!=0:
            return dp[n]
        dp[n] = self.calculateSteps(dp,n-1)+self.calculateSteps(dp,n-2)
        return dp[n]