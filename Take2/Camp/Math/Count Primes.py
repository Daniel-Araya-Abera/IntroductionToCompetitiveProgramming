class Solution:
    def countPrimes(self, n: int) -> int:
        count = [True] * n
        
        for num in range(2, len(count)):
            if count[num]:
                i = num * 2
                while i < len(count):
                    count[i] = False
                    i += num
        
        res = 0
        for i in range(2, len(count)):
            if count[i]:
                res += 1
        return res
    