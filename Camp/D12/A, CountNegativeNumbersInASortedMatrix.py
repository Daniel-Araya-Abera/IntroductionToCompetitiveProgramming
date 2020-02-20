# Count Negative Numbers in a Sorted Matrix
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        summ = 0
        for i in range(len(grid)):
            sizeOfRow = len(grid[i])
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    summ += sizeOfRow - j
                    break
        print("summ is ", summ)
        return summ