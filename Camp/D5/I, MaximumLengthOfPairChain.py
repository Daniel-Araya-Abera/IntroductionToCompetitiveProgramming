class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        self.sortBySecondElements(pairs)
        count = 1
        previous = pairs[0]
        for i in range(1, len(pairs)):
            if pairs[i][0] > previous[1]:
                count += 1
                previous = pairs[i]
        return count
        
    def swapPairs(self, pairs: List[List[int]]):
        for i in range(len(pairs)):
            pairs[i][0] , pairs[i][1] = pairs[i][1] , pairs[i][0]
    
    def sortBySecondElements(self, pairs):
        self.swapPairs(pairs)
        pairs.sort()    
        self.swapPairs(pairs)   
        
# Sample test cases
# [[1,2], [2,3], [3,4]]
# [[5,29], [10,30], [15,18], [20,25], [21,35], [22,40], [50,100]  ]