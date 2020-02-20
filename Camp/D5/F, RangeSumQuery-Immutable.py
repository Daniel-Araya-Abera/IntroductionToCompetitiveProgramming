# https://leetcode.com/problems/range-sum-query-immutable/
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        summ = 0
        for index in range(i, j + 1):
            summ += self.nums[index]
        print("summ is ", summ)
        return summ

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)