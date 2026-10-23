class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i, j = 0, len(nums) - 1

        while i <= j:
            mid = (i + j) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[i] <= nums[mid]:
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1

        return -1