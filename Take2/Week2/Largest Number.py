# Largest Number
# https://leetcode.com/problems/largest-number/
# Difficulty: Medium

class Solution:
    def compare(self,num1, num2):
        num1 = str(num1)
        num2 = str(num2)
        if num1[0] > num2[0]:
            return -1
        elif num1[0] < num2[0]:
            return 1
        else:
            if len(num1) == len(num2):
                if int(num1) >= int(num2):
                    return -1
                else:
                    return 1
            a, b = int(num1 + num2), int(num2 + num1)
            if a <= b: return 1
            return -1
        
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""
        nums_ordered = sorted(nums, key=functools.cmp_to_key(self.compare))
        
        queue = deque()
        for each in nums_ordered:
            queue.append(str(each))
            
        while queue and queue[0] == '0':
            queue.popleft()
        
        if not queue:
            return "0"                      
        return "".join(queue)
        
