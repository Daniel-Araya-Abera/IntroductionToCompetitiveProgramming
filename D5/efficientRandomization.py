import random

def generateRandomOrder():
    generatedList = []
    for i in range(1,10001):
        randIndex = random.randint(i,10000)
        generatedList.insert(randIndex,i)
    
    #print(generatedList)
    return generatedList