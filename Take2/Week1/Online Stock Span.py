# StockSpanner
# https://leetcode.com/problems/online-stock-span/
# Difficulty: Medium

class StockSpanner:

    def __init__(self):
        self.stockSpanner = []
        

    def next(self, price: int) -> int:
        if not self.stockSpanner:
            self.stockSpanner.append([price, 1])
            return 1

        if self.stockSpanner[-1][0] > price:
            self.stockSpanner.append([price, 1])
            return 1
        
        count = 1
        while self.stockSpanner:
            if self.stockSpanner[-1][0] <= price:
                curr = self.stockSpanner.pop()
                count += curr[1]
            else:
                break

        self.stockSpanner.append([price, count])
        return count
                
                
                
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)