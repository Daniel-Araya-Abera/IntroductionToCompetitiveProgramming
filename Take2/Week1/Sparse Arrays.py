# Sparse Arrays
# https://www.hackerrank.com/challenges/sparse-arrays/problem
# Difficulty: Medium

#!/bin/python3

def matchingStrings(strings, queries):
    freq = {}
    for each in strings:
        if each not in freq:
            freq[each] = 1
        else:
            freq[each] += 1
    
    result = [None] * len(queries)
    curr = 0
    for query in queries:
        result[curr] = freq[query] if query in freq else 0
        curr += 1
    return result

