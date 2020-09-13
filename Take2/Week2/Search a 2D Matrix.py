# Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/
# Difficulty: Medium

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        queue = deque()
        queue.append([0,0])
        neighbours = [[1,0],[0,1]]
        while queue:
            curr = queue.popleft()
            if matrix[curr[0]][curr[1]] == target:
                return True
            for each in neighbours:
                newX = curr[0] + each[0]
                newY = curr[1] + each[1]
                if 0 <= newX < len(matrix) and 0 <= newY < len(matrix[0]):
                    if matrix[newX][newY] < target:
                        queue.append([newX,newY])
                        break
                    elif matrix[newX][newY] == target:
                        return True
                    
        return False