# https://leetcode.com/problems/perfect-number/
import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sumOfDivisors = 1
        for divisor in range(2, int(num ** 0.5) + 1):
            moduloVal = num % divisor
            if not (moduloVal): # num is divisible
                sumOfDivisors += divisor + int( num / divisor )
            
        # print("sum of divisors : ", sumOfDivisors)
        # print("num is ", num)
        if num == sumOfDivisors:
            return True
        else:
            return False
            
                
s = Solution()
answer = s.checkPerfectNumber(28)
# answer = s.checkPerfectNumber(6)
# answer = s.checkPerfectNumber(8128)
print(answer)