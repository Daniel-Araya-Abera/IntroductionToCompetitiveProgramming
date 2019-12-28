def sortNumbers(a1,b1,c1):
    a = min(a1,b1,c1)
    c = max(a1,b1,c1)
    b = (a1 + b1 + c1) - a - c
    return a,b,c



def threeFriends(givenInput):
    input = givenInput.split("\n")
    input = input[1:]
    result = ""

    for i in range(len(input)):
        singleLine = input[i]    
        singleLine = singleLine.split()

        a = singleLine[0]
        b = singleLine[1]
        c = singleLine[2]
        a = eval(a)
        b = eval(b)
        c = eval(c)

        a,b,c = sortNumbers(a,b,c)
                   
        if a == b == c:
            a = b = c = 0
        elif a == b:
            a = a + 1
            b = b + 1
            if a < c:
                c = c - 1

        elif b == c:
            b = b - 1
            c = c - 1
            if a < b:
                a = a + 1
        else:
            a = a + 1
            b = b
            c = c - 1

        # if a < b:
        #     a = a + 1
        #     if b == c and a < b:
        #         b = b - 1
        #         c = c - 1
        #     if a == b and b < c:
        #         a = a + 1
        #         b = b + 1
        # if c > b:
        #     c = c - 1

        first = b - a
        second = c - b
        third = c - a
        summ = first + second + third

        if i < len(input) - 1 :
            result = result + str(summ) + "\n"
        else:
            result = result + str(summ)

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
    threeFriends(givenInput)
