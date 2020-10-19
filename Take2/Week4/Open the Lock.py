# Open the Lock
# https://leetcode.com/problems/open-the-lock/
# Difficulty: Medium

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadendsSet = set(deadends)
        
        neighbours = [1, -1]
        
        # state ->  (combination, count)
        start = "0000"
        if target == start:
            return 0
        if start in deadendsSet:
            return -1
        
        
        queue = deque()
        queue.append((start, 0))
        visited = set()
        visited.add((start))
        while queue:
            combination, count = queue.popleft()
            combination = list(combination)
            for i in range(len(combination)):
                for each in neighbours:
                    newCombination = combination[:]
                    updatedValue = (int(newCombination[i]) + each) % 10
                    newCombination[i] = str(updatedValue)
                    newCombination = "".join(newCombination)
                    if newCombination == target:
                        return count + 1
                    if newCombination not in visited:
                        if newCombination not in deadendsSet:
                            queue.append((newCombination, count + 1))
                        visited.add(newCombination)
        
        return -1
        