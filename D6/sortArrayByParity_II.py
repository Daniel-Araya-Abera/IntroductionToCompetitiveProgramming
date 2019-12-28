class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        count_odd = 1
        count_even = 0
        for i in range(len(A)):
            if not(A[i] % 2): #num is even
                result.insert(count_even,A[i])
                count_even = count_even + 2
                
            else:
                result.insert(count_odd,A[i])
                count_odd = count_odd + 2
        return result