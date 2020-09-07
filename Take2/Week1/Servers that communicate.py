# Servers that communicate
# https://leetcode.com/problems/count-servers-that-communicate/
# Difficulty: Medium

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = set()
        cols = set()
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    if i in rows or j in cols:
                        count += 1
                    else:
                        x = self.checkRows(i,j, grid)
                        y = self.checkCols(i,j, grid)
                        if x or y:
                            count += 1
                    rows.add(i)
                    cols.add(j)
        return count
                
    
    def checkRows(self,i,j, grid):
        for row in range(len(grid)):
            if grid[row][j] and row != i:
                return True
        
        return False
    
    def checkCols(self,i,j, grid):
        for col in range(len(grid[0])):
            if grid[i][col] and col != j:
                return True
        return False