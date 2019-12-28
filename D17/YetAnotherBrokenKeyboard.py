# Codeforces Round #605 (Div. 3)

def brokenKeyboard(givenInput):
    givenInput = givenInput.split("\n")
    
    inputInfo = givenInput[0]
    inputInfo = inputInfo.split()
    
    lengthOfString = eval(inputInfo[0])
    numOfWorkingKeys = eval(inputInfo[1])
 
    givenString = givenInput[1]
    # givenString = givenString.split()
 
    workingKeys = givenInput[2]
    workingKeys = workingKeys.split()
 
    summ = 0
    count = 0
    for i in range(len(givenString)):
        if givenString[i] in workingKeys:
            # print("FOUND , ", givenString[i], " IN ", workingKeys)
            count = count + 1
 
            if i == len(givenString) - 1 and count > 0:
                addend = int( ( count * (count + 1) ) / 2  )
                summ += addend
                count = 0
        else:
            if count > 0:
                addend = ( count * (count + 1) ) / 2
                summ += addend
                count = 0
  
    result = int(summ)
    return result
 
 
 
if __name__ == "__main__":
    inputInfo = input() #first line
    givenString = input() #second line
    workingKeys = input() #third line
 
    finalInput = inputInfo + "\n" + givenString + "\n" + workingKeys     
    # print("final input is ", finalInput)

    result = brokenKeyboard(finalInput)
    # print("result is ", result)
    print(result)