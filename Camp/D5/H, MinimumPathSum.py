# https://leetcode.com/problems/minimum-path-sum/
class Solution:
            
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                topSideIsValid = 0 <= i - 1 < len(grid)
                leftSideIsValid = 0 <= j - 1 < len(grid[i])
                
                if topSideIsValid and leftSideIsValid:                
                    topSide = grid[i - 1][j]
                    leftSide = grid[i][j - 1]
                    minn = min(topSide, leftSide)
                    grid[i][j] += minn
                
                if topSideIsValid and not leftSideIsValid:                
                    topSide = grid[i - 1][j]
                    grid[i][j] += topSide
                
                if not topSideIsValid and leftSideIsValid:                
                    leftSide = grid[i][j - 1]
                    grid[i][j] += leftSide
        n = len(grid)
        m = len(grid[0])
        return grid[n - 1][m - 1]