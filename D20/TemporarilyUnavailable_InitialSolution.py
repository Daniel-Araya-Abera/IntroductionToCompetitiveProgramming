def temporarilyUnavailableSingle(a,b,c,r):
    minLimit = min(a,b)
    maxLimit = max(a,b)
    a = minLimit
    b = maxLimit
    count = 0
    exclude = 0
 
    first = c - r
    second = c + r
    diff = b - a
    if first < a < b < second:
        count = 0
    if first <= a <= second and not(b < second):  #1,10,0,1
        exclude = second - a
        count = diff - exclude
    if first <= b <= second and not(first <= a <= second): #1,10,9,3
        # exclude = second - a
        exclude = b - first
        count = diff - exclude
    if a <= first and second <= b: #1,10,7,1
        exclude = second - first
        count = diff - exclude
    
    elif first >= b:  #1,10,20,1
        count = diff
 
    elif second <= a:   #1,10,20,1
        count = diff
    
    # print("count is ", count)
 
    return count
def temporarilyUnavailable(givenInput):
    input = givenInput.split("\n")
    input = input[1:]
    result = ""
 
    for i in range(len(input)):
        singleLine = input[i]    
        singleLine = singleLine.split()
 
        a = singleLine[0]
        b = singleLine[1]
        c = singleLine[2]
        r = singleLine[3]
        a = eval(a)
        b = eval(b)
        c = eval(c)
        r = eval(r)
 
        singleResult = temporarilyUnavailableSingle(a,b,c,r)
 
        if i < len(input) - 1 :
            result = result + str(singleResult) + "\n"
        else:
            result = result + str(singleResult)
 
    print(result)
 
if __name__ == "__main__":
    n = eval(input())
    givenInput = str(n) + "\n"
    
    for i in range(n):
        singleLine = input()
        if i == n - 1:
            givenInput += singleLine
            continue
        givenInput += singleLine + "\n"
    temporarilyUnavailable(givenInput)
 
# 8 2 10 100
# 2 3 2 3