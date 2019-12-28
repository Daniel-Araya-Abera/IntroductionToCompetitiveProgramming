class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        result = self.searchHelper(nums, start , end , target)
        return result
    
    def searchHelper(self, nums, start , end , target):
        mid = (start + end) // 2
        if target > nums[mid]:
            start = mid + 1
            return self.searchHelper(nums, start, end, target)
        elif target < nums[mid]:
            end = mid
            return self.searchHelper(nums, start, end, target)
        # else: # nums[mid] == target:
        #     return mid
            
    
# s = Solution()
# nums = [-1,0,3,5,9,12]
# target = 9
# ans = s.search(nums, target)
# print("ans is", ans)