class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequency = {} # this holds the frequency of each characters in the given list
        for each in arr:
            if each not in frequency:
                frequency[each] = 1
            else:
                frequency[each] += 1
        # print("frequency is ", frequency)
        
        listOfAllFrequencies = []
        for each in frequency:
            if frequency[each] in listOfAllFrequencies:
                return False
            else:
                listOfAllFrequencies.append(frequency[each])
        return True