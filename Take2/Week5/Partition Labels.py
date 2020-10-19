# Partition Labels
# https://leetcode.com/problems/partition-labels/
# Difficulty: Medium

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        lastLettersIndex = [None] * 26
        for i in range(len(S)):
            lastLettersIndex[ord(S[i]) - ord('a')] = i
        
        res = []
        start = end = 0
        for i in range(len(S)):
            possibleMax = lastLettersIndex[ord(S[i]) - ord('a')]
            end = max(end, possibleMax)
            
            if i == end:
                res.append(end - start + 1)
                start = end = i + 1
        return res
        