class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # edges => 4 * n * m
        # nodes => n * m
        
        neighbours = ((1,0),(0,1),(-1,0),(0,-1))
        for i in range(len(board)):
            for j in range(len(board[i])):
                if word[0] == board[i][j]:
                    visited = set()
                    if self.dfs(board, word, 1, (i,j), visited, neighbours):
                        return True
        return False
    
    def dfs(self, board, word, index, point, visited, neighbours):
        if index == len(word):
            return True
        visited.add(point)
        
        found = False
        for neighbour in neighbours:
            x = neighbour[0] + point[0]
            y = neighbour[1] + point[1]
            if 0 <= x < len(board) and 0 <= y < len(board[0]):
                if word[index] == board[x][y] and (x,y) not in visited:
                    if self.dfs(board, word, index + 1, (x, y), visited, neighbours):
                        return True
        visited.remove(point)
        return found
