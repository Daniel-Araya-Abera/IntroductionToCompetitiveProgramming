# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i - 1] + nums[i] < nums[i]:
                # print("edge case at i = ",i)
                dp[i] = nums[i]
            else:
                # print("normal case at i = ", i)
                summ = dp[i - 1] + nums[i]
                dp[i] = summ
            
        # print("dp is now ", dp)
        return max(dp)