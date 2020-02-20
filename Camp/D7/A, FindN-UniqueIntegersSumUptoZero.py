# https://leetcode.com/contest/weekly-contest-169/problems/find-n-unique-integers-sum-up-to-zero/
class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n == 0:
            return result
        
        
        end = n
        if not n % 2: ## n is even
            end = n // 2 + 1
            for i in range(1, end):
                result.append(i)
                result.append(-i)
            # print("result is ", result)
            return result
        else:
            
            end = n // 2 + 1
            result.append(0)                
            for i in range(1, end):
                result.append(i)
                result.append(-i)
            # print("result is ", result)
            return result