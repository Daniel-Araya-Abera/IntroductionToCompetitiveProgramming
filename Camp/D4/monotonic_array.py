#First question
# https://leetcode.com/problems/monotonic-array/

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
        notIncreasing = notDecreasing = False
        
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                notIncreasing = True
            if A[i] < A[i + 1]:
                notDecreasing = True
        
        if notIncreasing == True and notDecreasing == True:
            return False
        elif notIncreasing == True and notDecreasing == False:
            return True
        
        elif notIncreasing == False and notDecreasing == True:
            return True
        
        elif notIncreasing == False and notDecreasing == False:
            return True
        # return notIncreasing or notDecreasing
        
        
        
        