class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        for i in range(len(s)):
            char_set = set()
            for j in range(i, len(s)):
                if s[j] in char_set:
                    break
                else:
                    char_set.add(s[j])
            maxlen = max(maxlen, len(char_set))
        return maxlen