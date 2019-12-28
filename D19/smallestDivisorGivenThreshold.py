class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start = 1
        end = nums[-1]
        currentResult = nums[-1]
        finalResult = self.smallestDivisorHelper(nums, start, end, threshold, currentResult)
        return finalResult
    def smallestDivisorHelper(self, nums, start, end, threshold, currentResult):
        if start == end or start > end :
            return currentResult
        mid = (start + end) // 2
        # print(" start: ", start, " and end : ", end)
        # print("mid : ",mid)
        summ = self.getDivisor(nums, mid)
        # print("summ IS ", summ)
        if summ <= threshold:
            currentResult = mid
            end = mid
            return self.smallestDivisorHelper(nums, start, end, threshold, currentResult)
        else:
            start = mid + 1
            return self.smallestDivisorHelper(nums, start, end, threshold, currentResult)
            
            
    def getDivisor(self, nums, mid):
        summ = 0
        for each in nums:
            temp = math.ceil( each / mid )
            # print("temp: ", temp)
            summ += temp
        return summ
        