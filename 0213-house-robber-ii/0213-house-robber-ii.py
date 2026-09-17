class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        memo1 = [-1]*n
        memo2 = [-1]*n
        return max(self.robHouse(0,(n-1),nums,memo1),self.robHouse(1,n,nums,memo2))
    def robHouse(self,f,l,house,dp):
        if f >= l:
            return 0
        if dp[f]!=-1:
            return dp[f]
        if (f<l):
            take = self.robHouse(f+2,l,house,dp)+house[f]
            skip = self.robHouse(f+1,l,house,dp)
        dp[f]= max(take,skip)
        return dp[f]