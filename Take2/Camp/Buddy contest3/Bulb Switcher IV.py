class Solution:
    def minFlips(self, target: str) -> int:
        count = 0
        
        for num in target:
            if num == "1" and count % 2 == 0:
                count += 1
            
            if num == "0" and count % 2 != 1:
                count += 1
        
        return count
            