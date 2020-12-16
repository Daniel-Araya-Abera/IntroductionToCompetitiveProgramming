'''
Given g -> greed factor of each child(size of cookie required to satisfy) and
      s -> size of each cookie available
Maximize the num of children we can satisfy

Algorithm: -> Greedily try and satisfy the children by first prioritizing children with smallest greed factor
----
Sort g, s
Use two pointers and if we find a cookie for a child increment count by 1, if not check next cookie in s 
till we run out of cookie or children

'''
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = cookie = 0
        count = 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                count += 1
                child += 1
                cookie += 1
            else:
                cookie += 1
        
        return count
