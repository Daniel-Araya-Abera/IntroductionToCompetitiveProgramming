## leetcode question
# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for each in nums1:
            for each2 in nums2:
                if each == each2 and each not in result:
                    result.append(each)
        return result
                