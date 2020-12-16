class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        first = self.myPow(x, n // 2)
        
        if not n % 2:
            return first * first
        return first * first * x
