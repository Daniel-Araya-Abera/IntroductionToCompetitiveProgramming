# https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:

        count = 0
        while n >= 5:
            temp = n = n // 5
            count += temp
        # print(count)
        return count
        