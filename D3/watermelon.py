def getWatermelons(givenInputInKilos):

    sum = 0
    factors = []

    for i in range(2,givenInputInKilos,2):
        if givenInputInKilos % 2 == 0:
            factors.append(i)
    #print(factors)

    for i in range(len(factors)):
        for j in range(len(factors)):
            if factors[i] + factors[j] == givenInputInKilos:
                return "YES"
    return "NO"

if __name__ == "__main__":
    value = eval(input())
    print(getWatermelons(value))

