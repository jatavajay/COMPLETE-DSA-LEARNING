from bisect import bisect_left
from bisect import bisect_right 
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        f = bisect_left(nums,target)
        e = bisect_right(nums,target)

        if f == e:
            return [-1, -1]

        return [f, e - 1]