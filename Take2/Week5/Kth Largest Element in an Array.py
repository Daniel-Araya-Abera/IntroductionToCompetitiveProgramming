# Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Difficulty: Medium

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heapreplace(heap, nums[i])
        
        return heap[0]