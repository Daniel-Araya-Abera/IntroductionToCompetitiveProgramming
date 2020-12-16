class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        start, end, alex_is_next = 0, len(piles) - 1, True
        dp = {}
        alex_sum, lee_sum = self.collectStone(piles,start,end,alex_is_next,dp)
        
        return alex_sum > lee_sum
    
    
    def collectStone(self, piles, start,end, alex_is_next,dp):
        if start == end:
            if alex_is_next:
                return [piles[start],0]
            return [0, piles[start]]
        
        state = (start,end, alex_is_next)
        
        if state in dp:
            return dp[state]
        
        left = self.collectStone(piles,start + 1, end, alex_is_next,dp)
        right = self.collectStone(piles,start, end - 1, alex_is_next,dp)
        
        res = left if left[0] > right[0] else right
        
        dp[state] = res
        return res
