from collections import defaultdict
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        neighbours = self.generate_indices(board)
        start, distance = 1,0
        end = len(board) * len(board[0])
        queue = deque([(start, distance)])
        visited = set([start])
        while queue:
            curr_position, curr_distance = queue.popleft()
            if curr_position == end:
                return curr_distance
            for neighbour in neighbours[curr_position]:
                new_position = neighbour
                if new_position > end:
                    break
                if new_position not in visited:
                    queue.append((new_position, curr_distance + 1))
                    visited.add(new_position)
        return -1
        
    def generate_indices(self, board):
        neighbours = defaultdict()
            j_start = 0
            j_end = len(board[0])
            step = 1
        else:
            j_start = len(board[0]) - 1
            j_end = -1
            step = -1
        
        
        while count > 0:
            for i in range(len(board)):
                for j in range(j_start, j_end,step):
                    for i in range()
                    if board[i][j] != -1:
                        curr_num = count
                        neighbours[curr_num].append(board[i][j])
                        
                    
                    for next_neighbour in range(count + 1, count + 7):
                        if next_neighbour > len(board):
                            break
                        if next_neighbour not in match:
                            neighbours[count].append(next_neighbour)
                        
                        neighbours[count].append(match[next_neighbour])
                        
                        
                        
                    count -= 1
                j_start, j_end = j_end, j_start
                
                if j_end == 0:
                    j_start -= 1
                    j_end -= 1
                    step = -1
                else:
                    j_start += 1
                    j_end += 1
                    step = 1
        return neighbours
