# https://leetcode.com/problems/perfect-number/
import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sumOfDivisors = 0
        # endpoint = num // 2 + 1
        # print("end point ", num // 2 + 1)
        for divisor in range(1, num // 2 + 1):
            moduloVal = num % divisor
            if not (moduloVal): # num is divisible
                sumOfDivisors += divisor
            
        # print("sum of divisors : ", sumOfDivisors)
        # print("num is ", num)
        if num == sumOfDivisors:
            return True
        else:
            return False
            
                
s = Solution()
answer = s.checkPerfectNumber(28)
print(answer)