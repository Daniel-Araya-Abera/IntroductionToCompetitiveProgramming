# Group the People Given the Group Size They Belong To
# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
# Difficulty: Medium

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        count = [[] for i in range(max(groupSizes) + 1)]
        
        for i in range(len(groupSizes)):
            count[groupSizes[i]].append(i)       
        
        res = []
        for i in range(1, len(count)):
            newItems = []
            for j in range(0, len(count[i]), i):
                curr = count[i][j:j+i]
                temp = []
                temp.append(curr)
                res.extend(temp)
        return res
            