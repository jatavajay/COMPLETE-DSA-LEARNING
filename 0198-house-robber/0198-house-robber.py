class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        return self.robHouse(dp, nums, n - 1)

    def robHouse(self, dp, nums, n):
        if n < 0:
            return 0
        if dp[n] != -1:
            return dp[n]
        take = self.robHouse(dp, nums, n - 2) + nums[n]
        skip = self.robHouse(dp, nums, n - 1)
        dp[n] = max(take, skip)
        return dp[n]