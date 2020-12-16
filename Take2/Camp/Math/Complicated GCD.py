def findGCD(a, b):
    if a == b:
        return a
    return 1
 
def main():
    curr_input = input()
    curr_input = curr_input.split()
    res = findGCD(curr_input[0], curr_input[1])
    print(res)
 
if __name__ == "__main__":
    main()
