class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        normalFrequency = {}
        for i in range(len(arr)):
            if arr[i] not in normalFrequency:
                normalFrequency[arr[i]] = 1
            else:
                normalFrequency[arr[i]] += 1
        # print("normal frequency is ", normalFrequency)
        
        frequency = {}
        for each in normalFrequency:
            if normalFrequency[each] not in frequency:
                newList = []
                newList.append(each)
                frequency[normalFrequency[each]] = newList
            else:
                frequency[normalFrequency[each]].append(each)
        
        # print("frequency is ", frequency)
        
#         print("starting  with sorted printing ")
        
        
        
#         for each in sorted(frequency, reverse=True):
#             print("each IS ", each, " frequency is ", frequency[each])
#         print("done with sorted printing ")
        # count = 0
        # summ = 0
        # sizeOfList = len(arr)
        # halfSize = sizeOfList // 2
#         for each in sorted(frequency.keys()):
#             print("EACH IS ", each)
#             for i in range(len(frequency[each])):
#                 if summ < halfSize:
#                     summ += each
#                     count += 1
#                     print("added each ", each)
#                 else:
#                     print("returning count ", count)
#                     return count

        temp = []
        for each in sorted(frequency.keys()):
            for i in range(len(frequency[each])):
                temp.append(each)
        # print("temp is ", temp)

        
        count = 0
        summ = 0
        sizeOfList = len(arr)
        halfSize = sizeOfList // 2
        for k in range(len(temp) - 1, -1 , -1):
            print("k ", temp[k])
            if summ < halfSize:
                summ += temp[k]
                count += 1
                # print("added each ", temp[k])
            else:
                # print("returning count ", count)
                return count
        # print("ANOTHER LINE returning count ", count)
        return count