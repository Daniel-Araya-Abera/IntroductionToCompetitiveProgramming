class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        mid = len(A) // 2
        
        if A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
            return mid
        elif A[mid] > A[mid - 1]:
            return mid + self.peakIndexInMountainArray(A[mid:])
        else: #A[mid] < A[mid - 1]:
            return self.peakIndexInMountainArray(A[:mid + 1])
            
        
        # for i in range(len(A)):
        #     if A[i] > A[i + 1]:
        #         return i