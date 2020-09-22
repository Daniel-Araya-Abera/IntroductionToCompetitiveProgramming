# The Full Counting Sort
# https://leetcode.com/problems/search-a-2d-matrix/
# Difficulty: Medium

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    original = arr[:]
    count = [[] for i in range(1000001)]
    mid = len(arr) // 2
    for i in range(len(arr)):
        each = arr[i]
        index = int(each[0])
        value = each[1]
        if i < mid:
            count[index].append("-")
        else:
            count[index].append(value)

    res = [None] * len(arr)
    curr = 0
    for each in count:
        if each:
            for item in each:
                res[curr] = item
                curr += 1
    res = " ".join(res)
    print(res)

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
