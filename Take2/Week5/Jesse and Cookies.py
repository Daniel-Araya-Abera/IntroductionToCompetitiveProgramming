# Jesse and Cookies
# https://www.hackerrank.com/challenges/jesse-and-cookies/problem
# Difficulty: Easy

#!/bin/python3

import os
import sys
import heapq

def cookies(k, A):
    if not k or not A:
        return 0
    count = 0
    heap = A[:]
    heapq.heapify(heap)
    while len(heap) > 1:
        first = heapq.heappop(heap)
        if first >= k:
            return count
        second = heapq.heappop(heap)
        newVal = first * 1 + second * 2
        heapq.heappush(heap, newVal)
        count += 1
    
    if heap:
        lastItem = heapq.heappop(heap)
        if lastItem >= k:
            return count
        return -1
    return -1


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
