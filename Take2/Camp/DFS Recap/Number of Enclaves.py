class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        n = len(A) - 1
        m = len(A[0]) - 1
        neighbours = ((1,0), (0,1), (-1,0), (0,-1))
        for i in range(len(A)):
            if A[i][0] == 1:
                self.dfs(i,0, A, neighbours)
        for i in range(len(A)):    
            if A[i][m] == 1:
                self.dfs(i,m, A, neighbours)
        for j in range(len(A[0])):
            if A[0][j] == 1:
                self.dfs(0,j, A, neighbours)
        for j in range(len(A[0])):
            if A[n][j] == 1:
                self.dfs(n,j, A, neighbours)
        
        summ = 0
        for row in A:
            summ += sum(row)
        return summ
    
    def dfs(self, row, col, A, neighbours):
        A[row][col] = 0
        for neighbour in neighbours:
            new_x = row + neighbour[0]
            new_y = col + neighbour[1]
            if 0 <= new_x < len(A) and 0 <= new_y < len(A[0]):
                if A[new_x][new_y] == 1:
                    self.dfs(new_x, new_y, A, neighbours)
