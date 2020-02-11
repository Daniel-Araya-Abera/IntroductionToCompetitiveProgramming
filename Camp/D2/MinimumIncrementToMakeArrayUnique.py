class Solution:    
    def sortList(self,arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[j] > arr[i]:
                    arr[j], arr[i] = arr[i], arr[j]
        return arr
               
    def minIncrementForUnique(self, A: List[int]) -> int:
        # sortedA = self.sortList(A)
        sortedA = sorted(A)
        # print("sortedA is ", sortedA)
        count = 0
        # print("LEN OF SORTED A IS " , len(sortedA))
        for i in range(1, len(sortedA)):
            if sortedA[i] <= sortedA[i - 1]:
                # print("at i = ", i, "sorted A[i] ", sortedA[i])
                required = sortedA[i - 1] + 1
                diff = required - sortedA[i]
                count += diff
                sortedA[i] = sortedA[i - 1] + 1
                # print(" required ", required , " diff is ", diff, "count is ", count)
                # print("CURRENT LIST AFTER I = ", i , " is ", sortedA)

        # print("count is ", count)
        return count