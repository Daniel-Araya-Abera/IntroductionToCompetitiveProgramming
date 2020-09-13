# Sqrt(x)
# https://leetcode.com/problems/sqrtx/
# Difficulty: Medium

class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        if x == 1:
            return 1
        if start * start == x:
            return start
        if end * end == x:
            return end
        
        while start < end:
            mid = (start + end) // 2
            print("mid is ", mid)
            if start == mid:
                return start
            
            if mid * mid == x:
                return mid
            elif mid * mid <= x:
                start = mid
            else:
                end = mid
            
        
        return start