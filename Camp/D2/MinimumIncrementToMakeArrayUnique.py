class Solution:    
    def sortList(self,arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[j] > arr[i]:
                    arr[j], arr[i] = arr[i], arr[j]
        return arr
               
    def minIncrementForUnique(self, A: List[int]) -> int:
        sortedA = sorted(A)
        count = 0
        for i in range(1, len(sortedA)):
            if sortedA[i] <= sortedA[i - 1]:
                required = sortedA[i - 1] + 1
                diff = required - sortedA[i]
                count += diff
                sortedA[i] = sortedA[i - 1] + 1
        return count