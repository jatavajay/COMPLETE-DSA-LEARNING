class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0
        while i<n:
            correct_idx = nums[i]-1
            if (1 <= nums[i] <= n and
                nums[i] != nums[correct_idx]):
                nums[i], nums[correct_idx] = (
                    nums[correct_idx], nums[i]
                )
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1