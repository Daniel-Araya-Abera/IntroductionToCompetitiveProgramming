def triangle1(size):
    for i in range(size):
        for j in range(i + 1):
            print("*",end = "")
        print()

triangle1(5)