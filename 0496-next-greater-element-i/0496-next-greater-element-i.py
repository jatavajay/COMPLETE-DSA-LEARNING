class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        for i in range (len(nums1)):
            Found = False
            for j in nums2:
                if j==nums1[i]:
                    Found=True
                elif Found and j>nums1[i]:
                    ans.append(j)
                    break
            else:
                ans.append(-1)
        return ans