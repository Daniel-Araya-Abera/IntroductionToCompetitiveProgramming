# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        #state = root, depth
        
        level_sum = [0]
        queue = deque([(root,1)])
        while queue:
            curr_node, curr_level = queue.popleft()
            if curr_level == len(level_sum):
                level_sum.append(curr_node.val)
            else:
                level_sum[curr_level] += curr_node.val
        
            if curr_node.left:
                queue.append((curr_node.left, curr_level + 1))
                
            if curr_node.right:
                queue.append((curr_node.right, curr_level + 1))
        
        max_sum,max_level = level_sum[1],1

        for i in range(2, len(level_sum)):
            if level_sum[i] > max_sum:
                max_sum = level_sum[i]
                max_level = i
        
        return max_level
        