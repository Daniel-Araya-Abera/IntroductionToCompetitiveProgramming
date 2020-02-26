# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = deque()
        queue.append( (0, root) )
        leftMostValues = { 0:root.val}
        
        while queue:
            current = queue.popleft()
            
            if current:
                leftSide = current[1].left
                rightSide = current[1].right

                if leftSide:
                    queue.append(    (current[0] + 1, current[1].left )   ) 

                    if (current[0] + 1) not in leftMostValues:
                        leftMostValues[current[0] + 1] = current[1].left.val

                if rightSide:
                    queue.append(    (current[0] + 1, current[1].right )   ) 
                    if (current[0] + 1) not in leftMostValues:
                        leftMostValues[current[0] + 1] = current[1].right.val
        maxx = max(leftMostValues.keys())
        return leftMostValues[maxx]
    
    
    
    