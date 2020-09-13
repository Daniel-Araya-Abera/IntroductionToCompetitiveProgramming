# Search Insert Position
# https://leetcode.com/problems/search-insert-position/
# Difficulty: Medium

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if nums[-1] < target:
            return len(nums)
        
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid + 1
        
        return start

    
    