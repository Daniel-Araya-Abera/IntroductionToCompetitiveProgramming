# https://leetcode.com/problems/triangle/
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        minPathSum = 0
        
        
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                minNum = min(triangle[i + 1][j] , triangle[i + 1][j + 1])
                triangle[i][j] += minNum
        
        print("triangle is ", triangle)
        
        
        return min(triangle[0])