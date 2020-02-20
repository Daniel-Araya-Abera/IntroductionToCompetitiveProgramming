class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]    # dp[1] = min (cost[0], cost[1])

        for i in range(2,len(cost)):
            minn = min(dp[i - 1], dp[i - 2])
            dp[i] = minn + cost[i]
        # print("costs: ", cost)
        # print("printing costs dp ", dp)
        return min(dp[-1], dp[-2])
        