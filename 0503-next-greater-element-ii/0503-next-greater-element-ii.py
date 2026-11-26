class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        res = []
        for i in range (len(nums)):
            for j in nums[i:]+nums[:i]:
                if j>nums[i]:
                    res.append(j)
                    break
            else:
                res.append(-1)
        return res
