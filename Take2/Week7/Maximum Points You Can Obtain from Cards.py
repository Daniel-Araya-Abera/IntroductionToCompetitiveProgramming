'''
form prefix sum and suffix sum

[1, 2, 3, 4, 5, 6, 1], k = 3
[1, 3, 6, 10,15,21,22]
[22,21,19,16,12,7, 1]

'''
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == 1:
            return cardPoints[0]
        
        prefix_sum = [0] * len(cardPoints)
        suffix_sum = [0] * len(cardPoints)
        prefix_sum[0] = cardPoints[0]
        suffix_sum[-1] = cardPoints[-1]
        
        for i in range(1,len(cardPoints)):
            prefix_sum[i] = prefix_sum[i - 1] + cardPoints[i]
            
        for i in range(len(cardPoints) - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + cardPoints[i]
        

        maxx = suffix_sum[len(prefix_sum) - k]
        for i in range(k):
            summ = prefix_sum[i]
            remaining = k - (i + 1)
            n = len(prefix_sum)
            index = n - remaining
            if 0 <= index < len(suffix_sum):
                summ += suffix_sum[index]
            
            maxx = max(maxx, summ)
        
        return maxx
