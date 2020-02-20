# https://leetcode.com/problems/unique-paths/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []
        for i in range(n):
            grid.append([])
        grid[0] = [1] * m
        for i in range(1, n):
            grid[i] = [0] * m
        
        for i in range(n):
            grid[i][0] = 1
        
        for i in range(1,n):
            for j in range(1,m):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        print("grid is ", grid)
        print("result is ", grid[n - 1][m - 1])
        return grid[n - 1][m - 1]