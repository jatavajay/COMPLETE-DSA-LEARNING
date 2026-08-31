class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return not (len(nums)==len(set(nums)))
        # OR
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
