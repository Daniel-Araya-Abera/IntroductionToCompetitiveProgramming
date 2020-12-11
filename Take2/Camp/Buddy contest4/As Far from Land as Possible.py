from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        land_count = 0
        water_count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    land_count += 1
                else:
                    water_count += 1
        
        if not land_count or not water_count:
            return -1
        
        queue = deque()
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_dist = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    queue.append(((i, j, 0)))
        
        while queue:
            row, col, dist = queue.popleft()
            
            max_dist = max(max_dist, dist)
            
            for neighbour in neighbours:
                new_row = row + neighbour[0]
                new_col = col + neighbour[1]
                if 0 <= new_row < len(grid) and \
                    0 <= new_col < len(grid[0]) and \
                     grid[new_row][new_col] == 0:
                    queue.append((new_row, new_col, dist + 1))
                    grid[new_row][new_col] = 1
        
        return max_dist
        