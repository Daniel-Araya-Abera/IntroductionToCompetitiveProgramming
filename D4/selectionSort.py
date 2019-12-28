import random
def selectionSort(givenList):
    for i in range(len(givenList)):
        minIndex = i
        for j in range(i + 1,len(givenList)):
            if givenList[minIndex] > givenList[j]:
                minIndex = j
        givenList[minIndex], givenList[j] = givenList[j] = givenList[minIndex]

    return givenList


def generateRandomOrder():
    generatedList = []
    for i in range(10000):
        randIndex = random.randint(0,10000)
        generatedList.insert(randIndex,i)

    return generatedList


randomList = generateRandomOrder()
#print(selectionSort([6,2,4,1,5,8,7,3]))
#print(selectionSort(randomList))
#print(randomList)

selectionSort(randomList)
