# Recursive Digit Sum
# https://www.hackerrank.com/challenges/recursive-digit-sum/problem
# Difficulty: Medium

#!/bin/python3

import math
import os
import random
import re
import sys

def superDigit(n, k):
    num = int(n)
    while num >= 10: ## two or more digits
        summ = 0
        for each in str(num):
            summ += int(each)
        summ *= k
        if summ < 10:
            return summ
        num = summ
        k = 1



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
