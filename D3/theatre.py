def setFlagStone(n,m,a):    
    remainder1 = n % a
    first = n // a 
    
    remainder2 = m % a
    second = m // a

    if remainder1 != 0 :
        first = first + 1
    if remainder2 != 0:
        second = second + 1
    return first * second


#print(setFlagStone(6,6,4))

if __name__ == "__main__":
    n = input().split()
    print(setFlagStone(int(n[0]), int(n[1]), int(n[2])))
    
