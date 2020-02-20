class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraphList = []
        anotherLIST = paragraph.split()
        punctuations = "!?',;."
        
        curr = ""
        for eachChar in paragraph:
            if eachChar not in punctuations and eachChar != " ":
                curr += eachChar
            else:
                if curr != "":
                    paragraphList.append(curr)
                curr = ""
        if curr != "":
            paragraphList.append(curr)
        
        
        for i in range(len(paragraphList)):
            if paragraphList[i][-1] in punctuations:
                paragraphList[i] = paragraphList[i][:len(paragraphList[i]) - 1]
        for i in range(len(paragraphList)):
            paragraphList[i] = paragraphList[i].lower()
        
        frequency = {}
        for each in paragraphList:
            if each not in frequency:
                 if each not in banned:
                        frequency[each] = 1
            else:
                frequency[each] += 1
        sortedFrequency = sorted(frequency.items() , reverse=True, key=lambda x: x[1])
        for each in sortedFrequency:
            return each[0]