# Sort an Array
# https://leetcode.com/problems/sort-an-array/
# Difficulty: Medium

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        size = 100001
        count = [0] * size
        for each in nums:
            index = each
            if index < 0:
                newIndex = index + size
                count[newIndex] += 1
            else:
                count[index] += 1
        
        start = size // 2 + 1
        res = [None] * len(nums)
        curr = 0
        for index in range(start, len(count)):
            while count[index]:
                num = index - size
                res[curr] = num
                curr += 1
                count[index] -= 1
        
        for index in range(start):
            while count[index]:
                num = index
                res[curr] = num
                curr += 1
                count[index] -= 1
        
        return res
