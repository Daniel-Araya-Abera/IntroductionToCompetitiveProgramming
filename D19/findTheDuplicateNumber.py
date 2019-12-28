class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        collection = {}
        for each in nums:
            if each not in collection:
                collection[each] = 1
            else:
                return each