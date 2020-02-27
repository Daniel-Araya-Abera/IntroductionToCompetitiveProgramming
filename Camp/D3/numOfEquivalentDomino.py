# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d),
#  or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].
# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
# numEquivDominoPairs

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        stack = []
        frequency = {}
        count = 0

        for i in range(len(dominoes)):
            if dominoes[i][0] > dominoes[i][1]:
                first = dominoes[i][0]
                second = dominoes[i][1]
                dominoes[i][0] = second
                dominoes[i][1] = first        
        
        for each in dominoes:
            eachTuple = tuple(each)
            if eachTuple not in frequency:
                frequency[eachTuple] = 1
            else:
                frequency[eachTuple] += 1
        
        for each in frequency:
            countSingle = frequency[each]
            count += int( ( countSingle * (countSingle - 1) ) / 2 )
        
        return count
