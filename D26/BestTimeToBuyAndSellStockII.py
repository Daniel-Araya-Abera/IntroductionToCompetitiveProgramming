class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        startIndex = 0
        endIndex = 0
        maxProfit = 0
        for i in range(len(prices) - 1):
            if prices[i] >= prices[i + 1]: startIndex = i + 1
            else:
                singleProfit = prices[i + 1] - prices[i]
                maxProfit += singleProfit    
        return maxProfit