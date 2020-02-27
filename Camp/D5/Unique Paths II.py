# https://leetcode.com/problems/unique-paths-ii/
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        if obstacleGrid[n - 1][m - 1] == 1:
            return 0
        
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1

        for j in range(m):
            if obstacleGrid[0][j] != -1:
                obstacleGrid[0][j] = 1
        for i in range(n):
            if obstacleGrid[i][0] != -1:
                obstacleGrid[i][0] = 1

        # print("grid is ", obstacleGrid)
        
        self.fixFirstColumnAfterObstacles(obstacleGrid,n)
        self.fixFirstRowAfterObstacles(obstacleGrid,m)
        
        # print("grid is ", obstacleGrid)
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j] == -1:
                    continue
                summ = 0
                if obstacleGrid[i - 1][j] != -1:
                    summ += obstacleGrid[i - 1][j]
                if obstacleGrid[i][j - 1] != -1:
                    summ += obstacleGrid[i][j - 1]
                obstacleGrid[i][j] = summ

        return obstacleGrid[n - 1][m - 1]
    
    
    def fixFirstRowAfterObstacles(self, obstacleGrid: List[List[int]],m):
        visitedObstacle = False
        for j in range(m):
            if visitedObstacle and obstacleGrid[0][j] != -1:
                obstacleGrid[0][j] = 0
            if obstacleGrid[0][j] == -1:
                visitedObstacle = True
                
    def fixFirstColumnAfterObstacles(self, obstacleGrid: List[List[int]],n):
        visitedObstacle = False
        for i in range(n):    
            if visitedObstacle and obstacleGrid[i][0] != -1:
                obstacleGrid[i][0] = 0
            if obstacleGrid[i][0] == -1:
                visitedObstacle = True
               