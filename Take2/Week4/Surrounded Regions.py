# Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/
# Difficulty: Medium

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ## go to all four edge lines and do dfs to find all unsurrounded regions and mark them as "A"
        # (the rest "O"s are surrounded regions)
        ## go over the board and mark all "O" to "X"
        ## change all unsurrounded regions "A" to "O"
        
        if not board:
            return 0
        rows_end = len(board) - 1
        cols_end = len(board[0]) - 1
        for i in range(len(board)):
            if board[i][0] == "O": ## leftmost
                self.dfs((i,0) , board)
            if board[i][cols_end] == "O": ## rightmost
                self.dfs((i,cols_end), board)
        
        for i in range(len(board[0])):
            if board[0][i] == "O": ## top most
                self.dfs((0, i) , board)
            if board[rows_end][i] == "O": ## bottom most
                self.dfs((rows_end, i), board)
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "A":
                    board[i][j] = "O"

    
    def dfs(self, coordinate, board):
        x,y = coordinate
        neighbours = [(1,0),(0,1),(-1,0),(0,-1)]
        stack = []
        stack.append((x,y))
        while stack:
            x,y = stack.pop()
            board[x][y] = "A"
            
            for neighbour in neighbours:
                newX = neighbour[0] + x
                newY = neighbour[1] + y
                if 0 <= newX < len(board) and 0 <= newY < len(board[0]):
                    if board[newX][newY] == "O":
                        stack.append((newX,newY))
                        