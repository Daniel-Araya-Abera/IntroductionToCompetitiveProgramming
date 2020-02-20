# The K Weakest Rows in a Matrix
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        frequency = {}
        for i in range(len(mat)):
            singleLine = mat[i]
            count = 0
            for each in singleLine:
                if each == 1:
                    count += 1
                
                    
            
            if count not in frequency:
                newList = []
                newList.append(i)
                frequency[count] = newList
            else:
                frequency[count].append(i)
        
#         print("frequency ", frequency)
        
#         print("printing each sorted based on keys : ")
        
        result = []
        countK = 0
        for each in sorted(frequency.keys()):
            # print("each is ", each, " and list is ", frequency[each])
            for eachIndex in frequency[each]:
                if countK < k:
                    # print("appended ", eachIndex, " in frequency[each] : ", frequency[each])
                    result.append(eachIndex)
                    
                    countK += 1
                    
        # print("result is ", result)
        return result