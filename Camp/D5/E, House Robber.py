# https://leetcode.com/problems/house-robber/
class Solution:
    def rob(self, nums: List[int]) -> int:
        x = self.robFrom(nums, 0)
        y = self.robFrom(nums, 1)
        return max(x, y)
    
    def robFrom(self, nums: List[int], startIndex) -> int:
        size = len(nums)
        if startIndex == size - 1:
            return nums[size - 1]
        if startIndex > size - 1:
            return 0
        end1 = startIndex + 1
        end2 = startIndex + 2
        if end1 == size - 1:
            return nums[end1] - nums[startIndex] ## also means nums[size - 1] - nums[startIndex]
        first = self.robFrom(nums, end1)
        second = self.robFrom(nums, end2)
        return nums[startIndex] + max(first, second)