# https://leetcode.com/problems/integer-break/
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp =[0,0,1,2,4,6,9]
        
        for i in range(7,n+1):
            dp.append(dp[i-3] * 3)
        return dp[n]