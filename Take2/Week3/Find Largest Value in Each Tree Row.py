# Find Largest Value in Each Tree Row
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# Difficulty: Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        maxx = -float('inf') ## can start at 0 too
        result = []
        queue = deque()
        queue.append([root,0])
        prevItem = [root.val, 0]
        while queue:            
            curr = queue.popleft()
            node, row = curr[0], curr[1]
            if node.left:
                queue.append([node.left, row + 1])
            if node.right:
                queue.append([node.right, row + 1])
            
            if row > prevItem[1]:
                ## new row found -> meaning we should add the prev row largest value
                result.append(prevItem[0])
                prevItem = [node.val, row]
            else:
                prevItem[0] = max(prevItem[0], node.val)
        
        ## add the last row largest element(number)
        result.append(prevItem[0])
        return result
    