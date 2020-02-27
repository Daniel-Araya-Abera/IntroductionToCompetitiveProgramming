from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        
        neighbour = [ [1,0], [0,1], [0,-1],[-1,0] ]
        queue = deque()
        queue.append([sr,sc])
        oldColor = image[sr][sc]
        ##BFS
        while queue: 
            lastElement = queue.popleft()
            currentX = lastElement[0]
            currentY = lastElement[1]
            image[currentX][currentY] = newColor
            
            for each in neighbour:
                x = currentX + each[0]
                y = currentY + each[1]
                if 0 <= x< len(image) and 0 <= y< len(image[0]) :
                    if image[x][y] == oldColor:
                        queue.append([x,y])
        return image