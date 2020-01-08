def countingSort(givenList):
    # countingList = [0] * len(givenList)
    maxVal = max(givenList)
    countingList = [0] * (maxVal + 1)
    result = []

    for i in range(len(givenList)):
        countingList[givenList[i]] += 1

    for index in range(len(countingList)):
        for j in range(countingList[index]):
            result.append(index)
    # print("countingList is " , countingList)
    # print("given list is:", givenList)
    # print("result is    :", result)
    return result
    
givenList = [1,4,1,2,7,5,2]

sortedList = countingSort(givenList)
print(sortedList)