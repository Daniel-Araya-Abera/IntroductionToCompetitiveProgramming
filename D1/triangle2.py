##isosceles triangle
#      *
#     ***
#    *****
#   *******
#  *********

def triangle2(size):
    for i in range(size):
        for j in range(size - i):
            print(" ", end= "")
        for k in range(2 * i + 1):
            print("*", end="")
        print()
triangle2(5)