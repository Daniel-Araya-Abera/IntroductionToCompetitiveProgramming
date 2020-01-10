def mezoPlayingZoma(givenInput):
    # result = givenInput
    moveLeftNum = moveRightNum = 0
    for each in givenInput:
        if each is "L":
            moveLeftNum += 1
        else:
            moveRightNum += 1
    
    result = moveLeftNum + moveRightNum + 1

    # print("result is ", result)
    # print("len is ", len(givenInput))
    return result
if __name__ == "__main__":
    n = eval(input())
    givenInput = str(n) + "\n"
    
    singleLine = input()
    numOfPossibleLocations = mezoPlayingZoma(singleLine)
    print(numOfPossibleLocations)
