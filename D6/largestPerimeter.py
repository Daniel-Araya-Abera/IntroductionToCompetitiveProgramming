class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        first = A[0]
        second = A[1]
        third = A[2]

        if first + second > third or second + third > first or third + first > second :
            return first + second + third
        return 0

        # largest = max(first,second,third)
        # smallest = min(first,second,third)
        # summ = first + second + third
        # medium = summ - smallest - largest

        # print("largest is ", largest)
        # print("smallest is ", smallest)
        # print("medium is ", medium)
        # if largest * largest == smallest * smallest + medium * medium:
        #     return first + second + third
        # return 0