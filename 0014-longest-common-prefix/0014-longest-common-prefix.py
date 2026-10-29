from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        min_len = min(len(s) for s in strs)
        common = ""
        for i in range(min_len):
            current_char = strs[0][i]
            for s in strs[1:]:
                if s[i] != current_char:
                    return common
            common += current_char
        return common
