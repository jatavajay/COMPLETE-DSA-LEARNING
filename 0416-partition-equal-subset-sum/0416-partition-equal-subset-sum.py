class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        return self.subsetSum(nums, target)

    def subsetSum(self, nums, target):
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        # If target is 0, we can always make it
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = (
                        dp[i - 1][j] or
                        dp[i - 1][j - nums[i - 1]]
                    )
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][target]
