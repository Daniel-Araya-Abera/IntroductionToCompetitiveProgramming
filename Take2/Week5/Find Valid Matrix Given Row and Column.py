# Find Valid Matrix Given Row and Column Sums
# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/
# Difficulty: Medium

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

        res = [[0 for j in range(len(colSum))] for i in range(len(rowSum))]
        
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                minn = min(rowSum[i], colSum[j])
                res[i][j] = minn
                rowSum[i] -= minn
                colSum[j] -= minn
        
        return res
