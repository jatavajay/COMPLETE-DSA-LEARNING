class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        curr=0
        for i in s:
            if i=="(":
                curr+=1
            elif i==")":
                curr-=1
            max_depth = max(max_depth,curr)
        return max_depth