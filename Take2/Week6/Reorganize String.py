# Reorganize String
# https://leetcode.com/problems/reorganize-string/
# Difficulty: Medium

class Solution:
    def reorganizeString(self, S: str) -> str:
        heap = []
        freq = {}
        for each in S:
            if each not in freq:
                freq[each] = 1
            else:
                freq[each] += 1
        
        for each in freq:
            heapq.heappush(heap, (-freq[each], each))
        
        res = []
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            
            if (-first[0] > 1):
                heapq.heappush(heap, (first[0] + 1, first[1]))
            
            res.append(first[1])
            res.append(second[1])

            if (-second[0] > 1):
                heapq.heappush(heap, (second[0] + 1, second[1]))
        
        if heap:
            last = heapq.heappop(heap)
            if -last[0] > 1 or (last[1] == res[-1]):
                return ""
            else:
                res.append(last[1])
        return "".join(res)
        