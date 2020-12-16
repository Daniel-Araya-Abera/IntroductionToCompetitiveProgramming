class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum_of_factors = self.sumOfFactors(num)
        return sum_of_factors == num
    
    
    def sumOfFactors(self, num):
        if num == 1:
            return 0
        summ = 1
        for i in range(2, int(num ** 0.5) + 1):
            if not num % i:
                summ += i
                summ += (num // i)
        return summ
