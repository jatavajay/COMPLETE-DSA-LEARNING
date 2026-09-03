class Solution {
    public int climbStairs(int n) {
        int[] dp = new int[n+1];
        return calculateStep(n, dp);
    }
    public int calculateStep(int n, int[] dp){
        if(n<=2) return n;
        if(dp[n]!=0) return dp[n];
        dp[n] = calculateStep(n-1, dp) + calculateStep(n-2, dp);
        return dp[n];
    }
}
