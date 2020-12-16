class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        smallest_path = len(grid) - 1 + len(grid[0]) - 1
        if k > smallest_path:
            # print("here")
            return smallest_path
        
        neighbours = ((1,0), (0,1), (0,-1), (-1,0))
        
        # state = point, distance, remaining_k, 
        queue = deque([((0,0), 0,k)])
        visited = set([((0,0), k)])
        m,n = len(grid), len(grid[0])
        
        while queue:
            curr_point, curr_distance, curr_k = queue.popleft()
            if curr_point == (m - 1, n - 1):
                return curr_distance
            for neighbour in neighbours:
                x = neighbour[0] + curr_point[0]
                y = neighbour[1] + curr_point[1]
                
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                    if grid[x][y] == 1:
                        if curr_k > 0:
                            if ((x,y),curr_k - 1) not in visited:
                                queue.append(((x,y),curr_distance + 1, curr_k - 1))
                                visited.add(((x,y), curr_k - 1))
                    else:
                        if ((x,y),curr_k) not in visited:
                            queue.append(((x,y),curr_distance + 1, curr_k))
                            visited.add(((x,y), curr_k))
        return -1
                    