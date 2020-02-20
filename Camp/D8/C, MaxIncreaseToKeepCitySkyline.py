# https://leetcode.com/contest/weekly-contest-77/problems/max-increase-to-keep-city-skyline/
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        summ = 0
        left = [-1] * len(grid)
        top = [-1] * len(grid)

        for i in range(len(grid)):
            left[i] = max(grid[i])
            for j in range(len(grid)):
                if grid[j][i] > top[i]:
                    top[i] = grid[j][i]
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                summ += ( min(left[i], top[j]) - grid[i][j])
        return summ
        