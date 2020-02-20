class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        return self.climbStairsHelper(n, dp)
    
    def climbStairsHelper(self, n: int, dp: List[int]) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        if dp[n - 1] == -1:
            dp[n - 1] = self.climbStairsHelper(n - 1, dp)
        
        if dp[n - 2] == -1:
            dp[n - 2] = self.climbStairsHelper(n - 2, dp)
        
        return dp[n - 1] + dp[n - 2]