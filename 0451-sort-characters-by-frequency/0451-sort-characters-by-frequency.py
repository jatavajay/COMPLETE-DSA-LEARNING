from operator import itemgetter
class Solution:
    def frequencySort(self, s: str) -> str:
        map = {}
        for ch in s:
            if ch in map:
                map[ch]+=1
            else:
                map[ch]=1
        output = ""
        sorted_d = dict(sorted(map.items(), key=itemgetter(1), reverse=True))
        for ch in sorted_d:
            for _ in range (sorted_d[ch]):
                output+=(ch)
        return output
