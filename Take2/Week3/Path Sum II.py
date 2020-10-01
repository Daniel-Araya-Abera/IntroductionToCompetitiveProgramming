# Path Sum II
# https://leetcode.com/problems/path-sum-ii/
# Difficulty: Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        
        res = []        
        queue = deque()
        queue.append([root, root.val, [root.val]])
        
        while queue:
            curr = queue.popleft()
            node, summ, path = curr[0], curr[1], curr[2]
                       
            if not node.left and not node.right and summ == sum:
                res.append(path)
                
            if node.left:
                newPath = path[:]
                newPath.append(node.left.val)
                queue.append([node.left, summ + node.left.val,newPath] )
            
            if node.right:
                newPath = path[:]
                newPath.append(node.right.val)
                queue.append([node.right, summ + node.right.val,newPath] )
                
        return res
        
