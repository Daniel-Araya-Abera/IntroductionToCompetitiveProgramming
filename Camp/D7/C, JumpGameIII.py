class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = {}
        if arr[start] == 0:
            return True
        currentBool = False
        i = arr[start]
        if 0 <= start - i <= len(arr) - 1:
            currentBool = currentBool or self.dfs(arr, start - i, visited)
        if 0 <= start + i <= len(arr) - 1:
            currentBool = currentBool or self.dfs(arr, start + i, visited)
        
        return currentBool
    
    def dfs(self, arr: List[int], start: int, visited) -> bool:
        if arr[start] == 0:
            return True
        currentBool = False    
        currentIndex = arr[start]
        temp = start - currentIndex
        if 0 <= start - currentIndex <= len(arr) - 1 and (temp not in visited):
            # currentBool = currentBool or self.dfs(arr, start - currentIndex)
            visited[temp] = 1
            if self.dfs(arr, start - currentIndex,visited): return True
            
        temp2 = start + currentIndex
        if 0 <= start + currentIndex <= len(arr) - 1 and ( temp2 not in visited):
            # currentBool = currentBool or self.dfs(arr, start + currentIndex)
            visited[temp2] = 1
            if self.dfs(arr, start + currentIndex,visited): return True
          
        return currentBool