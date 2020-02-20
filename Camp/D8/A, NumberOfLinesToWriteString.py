# https://leetcode.com/contest/weekly-contest-77/problems/number-of-lines-to-write-string/
import math
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        charIndexes = {'a': 0, 'b' : 1, 'c' : 2 , 'd' : 3,                                                  'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24                              ,'z':25}  

        if len(S) == 0:
            return 0
        
        lines = 1
        summ = 0
        for i in range(len(S)):
            char = S[i]
            index = charIndexes[char]
            if summ + widths[index] <= 100:
                summ += widths[index]
            
            else:
                summ = 0
                summ += widths[index]
                lines += 1
        result = [-1] * 2
        
        result[0] = lines
        result[1] = summ
        return result