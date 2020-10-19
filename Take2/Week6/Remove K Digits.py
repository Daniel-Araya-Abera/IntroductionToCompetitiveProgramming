# Remove K Digits
# https://leetcode.com/problems/remove-k-digits/
# Difficulty: Medium

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num:
            return "0"
        
        if len(num) == 1 and k == 1:
            return "0"
        if len(num) < k:
            return "0"
        stack = []
        count = 0
        stack.append(num[0])
        for i in range(1,len(num)):
            while stack and stack[-1] > num[i] and count < k:
                count += 1
                stack.pop()
            stack.append(num[i])
            
        while stack and count < k:
            count += 1
            stack.pop()
                
        if not stack:
            return "0"
        
        return str(int("".join(stack)))
            