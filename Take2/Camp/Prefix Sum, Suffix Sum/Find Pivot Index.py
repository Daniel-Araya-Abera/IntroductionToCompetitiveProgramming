class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        prefix_sum = [0] * len(nums)
        suffix_sum = [0] * len(nums)
        prefix_sum[0], suffix_sum[-1] = nums[0], nums[-1]
        
        end = len(nums) - 1
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
            suffix_sum[end - i] = suffix_sum[end - i + 1] + nums[end - i]
        
        for i in range(len(prefix_sum)):
            if prefix_sum[i] == suffix_sum[i]:
                return i
        return -1
