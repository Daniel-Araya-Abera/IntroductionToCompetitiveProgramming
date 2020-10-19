# Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/
# Difficulty: Medium

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        
        for each in s:
            if each not in freq:
                freq[each] = 1
            else:
                freq[each] += 1
        
        freq_descending = OrderedDict(sorted(freq.items(), key = lambda x: x[1], reverse = True))
        res = []
        for each in freq_descending:
            res.extend([each]*freq_descending[each])
        
        return "".join(res)
        