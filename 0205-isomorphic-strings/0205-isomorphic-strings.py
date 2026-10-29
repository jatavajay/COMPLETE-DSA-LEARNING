class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        for i in range(len(s)):
            if s[i] not in mapping:
                if t[i] in mapping.values():
                    return False  
                mapping[s[i]] = t[i]
        new_s = ''.join(mapping[c] for c in s)
        return new_s == t
