import random

def insertionSort(givenList):

    for i in range(len(givenList)):
        key = givenList[i]
        j = i-1
        while j >= 0 and key < givenList[j] : 
                givenList[j + 1] = givenList[j] 
                j -= 1
        givenList[j + 1] = key 

    return givenList


def generateRandomOrder():
    generatedList = []
    for i in range(1,10001):
        randIndex = random.randint(i,10000)
        generatedList.insert(randIndex,i)
    return generatedList
    #print(generatedList)

#print(insertionSort([6,2,4,1,5,8,7,3]))
#randomList = generateRandomOrder()
print(insertionSort(generateRandomOrder()))


