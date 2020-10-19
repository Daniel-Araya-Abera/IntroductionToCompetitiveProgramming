# Super Ugly Number
# https://leetcode.com/problems/super-ugly-number/
# Difficulty: Medium

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = primes[:]
        heap.append(1)
        visited = set(primes)
        visited.add(1)
        
        heapq.heapify(heap)
        
        count = 0
        topVal = None
        while count < n:
            topVal = heapq.heappop(heap)

            for prime in primes:
                newVal = prime * topVal
                if newVal not in visited:
                    heapq.heappush(heap, newVal)
                    visited.add(newVal)
            
            count += 1
            
        return topVal
        