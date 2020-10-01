# Bulls and Cows
# https://leetcode.com/problems/bulls-and-cows/
# Difficulty: Medium

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        visited = set()
        
        ## find bulls first
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                visited.add(i)
        
        count = [0 for i in range(10)]
        
        ## get available slots in count
        for i in range(len(secret)):
            if i not in visited:
                each = int(secret[i])
                count[each] += 1
        
        ## check if guess matches secret, excluding the bulls
        for i in range(len(guess)):
            if i not in visited:
                each = int(guess[i])
                if count[each] > 0:
                    count[each] -= 1
                    cows += 1  
        
        result = [str(bulls), "A", str(cows), "B"]
        return "".join(result)
        