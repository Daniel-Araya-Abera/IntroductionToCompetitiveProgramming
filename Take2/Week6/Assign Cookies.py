# Assign Cookies
# https://leetcode.com/problems/assign-cookies/
# Difficulty: Easy

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s:
            return 0
        g.sort()
        s.sort()
        count,currS = 0, 0
        
        while s[currS] < g[0]:
                currS += 1
        i = 0
        while i < len(g) and currS < len(s):
            if s[currS] >= g[i]:
                count += 1
                i += 1
            currS += 1
        return count
