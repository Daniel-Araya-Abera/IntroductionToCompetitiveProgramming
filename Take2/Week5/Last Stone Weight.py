# Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/
# Difficulty: Easy

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return stones[0] if stones else 0
        heap = []
        
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            diff = abs(first - second)
            if diff:
                heapq.heappush(heap, -diff)
        
        return -heap[0] if heap else 0
    