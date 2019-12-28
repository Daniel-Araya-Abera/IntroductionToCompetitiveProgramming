class Solution(object):

    def counting_sort(self, array, maxval):
        """in-place counting sort"""
        n = len(array)
        m = maxval + 1
        count = [0] * m               # init with zeros
        for a in array:
            count[a] += 1             # count occurences
        i = 0
        for a in range(m):            # emit
            for c in range(count[a]): # - emit 'count[a]' copies of 'a'
                array[i] = a
                i += 1
        return array

    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        visited = {}
        result = []
        restOfList = []
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    result.append(arr2[i])
                    visited[arr2[i]] = True
        
        for k in range(len(arr1)):
            if arr1[k] not in visited:
                # result.append(arr1[k])
                restOfList.append(arr1[k])

        #next round
        s = Solution()
        restOfListSorted = s.counting_sort(restOfList, 1001)  
        # result.append(restOfList)
        for each in restOfList:
            result.append(each)


        return result

Your Input  [2,3,1,3,2,4,6,7,9,2,19]
            [2,1,4,3,9,6]

Output [2,2,2,1,4,3,3,9,6,7,19]
Expected [2,2,2,1,4,3,3,9,6,7,19]