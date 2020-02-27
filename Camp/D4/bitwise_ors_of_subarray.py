class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        
        discoveredSumms = {}
        stack = []
        for i in range(len(A)):
            stack.append(A[i])
            for j in range(len(stack) - 1, -1 , -1):
                givenValue = stack.pop(j)
                calculatedResult = givenValue | A[i]
                if calculatedResult not in discoveredSumms:
                    discoveredSumms[calculatedResult] = set([i])
                    stack.append(calculatedResult)
                else:
                    if i not in discoveredSumms[calculatedResult]: 
                        discoveredSumms[calculatedResult].add(i)
                        stack.append(calculatedResult)
        return len(discoveredSumms)
                